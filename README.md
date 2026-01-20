# -birthday-card-
Check the file
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Happy Birthday, Mustuuu!</title>
    <style>
        body { font-family: Arial; background: #FFD700; text-align: center; padding: 20px; }
        .hidden { display: none; }
        .card { background: white; padding: 20px; border-radius: 10px; margin: 20px auto; max-width: 500px; }
        canvas { border: 1px solid #ccc; }
    </style>
</head>
<body>
    <div id="frame1" class="card">
        <h1>🎉 Happy Birthday, Mustuuu! 🎉</h1>
        <p>Hey Mustuuu, another year of awesomeness! You're not just my bestie, you're the guy who makes life brighter. Hope your birthday is filled with all the fun, laughter, and epic moments you deserve. Cheers to you!</p>
        <button onclick="showFrame('frame2')">Next: Cake Time!</button>
    </div>

    <div id="frame2" class="card hidden">
        <h2>🎂 Here's your cake! 🎂</h2>
        <canvas id="cakeCanvas" width="300" height="200"></canvas>
        <button onclick="cutCake()">Cut the Cake!</button>
    </div>

    <div id="frame3" class="card hidden">
        <h2>Here's your special gift!</h2>
        <button onclick="showFrame('frame4')">Click to Open!</button>
    </div>

    <div id="frame4" class="card hidden">
        <p>[Insert the full gift paragraph here]</p>
        <button onclick="showFrame('frame5')">Final Surprise!</button>
    </div>

    <div id="frame5" class="card hidden">
        <h2>Good day! Ty for coming into my life 💖</h2>
        <p>💖💗💓</p>
    </div>

    <script>
        function showFrame(id) {
            document.querySelectorAll('.card').forEach(el => el.classList.add('hidden'));
            document.getElementById(id).classList.remove('hidden');
        }

        function cutCake() {
            const canvas = document.getElementById('cakeCanvas');
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#8B4513';
            ctx.fillRect(100, 150, 100, 30);
            ctx.fillStyle = '#D2691E';
            ctx.fillRect(110, 130, 80, 20);
            ctx.fillStyle = '#F5DEB3';
            ctx.fillRect(120, 110, 60, 20);
            ctx.font = '30px Arial';
            ctx.fillText('🎂', 150, 100);
            ctx.strokeStyle = 'red';
            ctx.lineWidth = 5;
            ctx.beginPath();
            ctx.moveTo(150, 110);
            ctx.lineTo(150, 180);
            ctx.stroke();
            setTimeout(() => showFrame('frame3'), 2000);
        }
    </script>
</body>
</html>
