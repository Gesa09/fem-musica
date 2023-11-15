input.onButtonPressed(Button.A, function () {
    music.play(music.stringPlayable("A F E F D G E F ", 120), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.B, function () {
    music.play(music.stringPlayable("C5 B A G F E D C ", 120), music.PlaybackMode.UntilDone)
})
