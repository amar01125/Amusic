async function search() {
    const songName = document.getElementById("songInput").value;
    const player = document.getElementById("player");

    player.src = "/download?song=" + encodeURIComponent(songName);
    player.load();
    player.play();
}
