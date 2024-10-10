let draggedTask = null;

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.task-card').forEach(card => {
        card.addEventListener('dragstart', handleDragStart);
    });

    document.querySelectorAll('.column').forEach(column => {
        column.addEventListener('dragover', handleDragOver);
        column.addEventListener('drop', handleDrop);
    });
});

function handleDragStart(e) {
    draggedTask = e.target;
    e.dataTransfer.effectAllowed = 'move';
}

function handleDragOver(e) {
    e.preventDefault();
    e.dataTransfer.dropEffect = 'move';
}

function handleDrop(e) {
    e.preventDefault();

    const column = e.target.closest('.column');
    if (!column) return;

    const newStatus = column.getAttribute('data-status');
    const taskId = draggedTask.getAttribute('data-task-id');

    column.querySelector('.task-list').appendChild(draggedTask);

    updateTaskStatus(taskId, newStatus);
}

function updateTaskStatus(taskId, newStatus) {
    const csrfToken = document.getElementById('csrfToken').value;

    fetch(`/update_status/${taskId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ status: newStatus })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (!data.success) {
            console.error("Failed to update task status:", data.error);
        }
    })
    .catch(error => {
        console.error("Error updating task status:", error);
    });
}
