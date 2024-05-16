var socket = io();

socket.on('number_called', function(data) {
    document.getElementById('number').innerText = data.number;
});

function generateTicket() {
    fetch('/generate_ticket', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        var ticketDiv = document.getElementById('ticket');
        ticketDiv.innerHTML = '';
        data.ticket.forEach(row => {
            var rowDiv = document.createElement('div');
            row.forEach(num => {
                var numSpan = document.createElement('span');
                numSpan.innerText = num + ' ';
                rowDiv.appendChild(numSpan);
            });
            ticketDiv.appendChild(rowDiv);
        });
    });
}

function startGame(speed) {
    fetch('/start_game', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ speed: speed })
    });
}

function stopGame() {
    fetch('/stop_game', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    });
}
