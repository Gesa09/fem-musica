def on_button_pressed_a():
    if input.acceleration(Dimension.Y) != 90:
        music.play(music.string_playable("A F E F D G E F ", 1),
            music.PlaybackMode.UNTIL_DONE)
    else:
        music.play(music.string_playable("A F E F D G E F ", 120),
            music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if input.acceleration(Dimension.Y) < 90:
        music.play(music.string_playable("C5 B A G F E D C ", 1),
            music.PlaybackMode.UNTIL_DONE)
    else:
        music.play(music.string_playable("C5 B A G F E D C ", 120),
            music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)
