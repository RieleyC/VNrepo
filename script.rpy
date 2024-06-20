init python:
    ## Import random module to use unique random lists of numbers.
    import random

    def light_button():
        ##Lights up the required button to indicate the player should press.
        global random_button_indexes
        global current_button_index

        ## We're picking the next value in "random_button_indexes" every time this script runs.
        ## Add 1 to "current_button_index" to pick a value from the list.
        if current_button_index < buttons - 1:
            ## Add 1 to the variable as long as it isn't larger than the list size.
            current_button_index += 1
        else:
            ## The variable is the same size as the list, so we reset to 0 and get a new list.
            current_button_index = 0
            random_button_indexes = random.sample(range(6), k = 6)
        ## Set the randomly picked button states to lit instead of idle.
        random_button_index = random_button_indexes[current_button_index]
        button_state[random_button_index] = "lit"

    def game_buttonpress(btn):
        ## Runs when the player clicks a button.
        global score

        if button_state[btn] == "lit":
            ## If the button was lit, the score increases by 1.
            score += 1
            ## Reset button to idle.
            button_state[btn] = "idle"

    def setup_game():
        ## Function to set up the game
        global random_button_indexes

        for i in range(buttons):
            ## Fill the "button_state" function with idle values according to the number of buttons in that minigame.
            ## Every idle represents a button.
            button_state.append("idle")
            ## Regenerate a list of random button indexes.
            random_button_indexes = random.sample(range(buttons), k = buttons)

    def reset_game():
        ## Reset the game.
        global time1
        global score
        global countdown

        countdown = 5.0
        time1 = 30.0
        score = 0
        for i in range(buttons):
            button_state[i] = "idle"

        renpy.show_screen("countdown_timer")

## This declares a character to save space on letters.
define m = Character("Me")

## States of the button, either lit or idle.
default button_state = []

## Number of buttons in he minigame.
default buttons = 6

## The button index and which button(s) will change states
default random_button_indexes = []
default current_button_index = 0
default score = 0

## How long the minigame will last.
default time1 = 30

## How long the timer counts down before the game begins.
default countdown = 5

## Screen for when the game is over and time runs out.
screen game_over:
    frame:
        background "#000000"
        xfill True
        yfill False
        text "You've scored: [score]" size 50 text_align 0.5 align(0.5, 0.4)
        imagebutton idle "Try again.png" align(0.2, 0.8) action [Hide("game_over"), Function(reset_game)]
        imagebutton idle "Main menu.png" align(0.85, 0.8) action MainMenu()

## The timer for the countdown before the game starts.
screen countdown_timer:
    frame:
        background "#000000"
        xfill True
        yfill True
        text "[countdown]" size 120 text_align 0.5 align(0.5, 0.5)

    ## Timer to subtract 1.0 from the "countdown" variable. Hides this screen after the variable reaches 1.0
    timer 1.0 action If(countdown > 1, SetVariable("countdown", countdown - 1), Hide("countdown_timer")) repeat If(countdown > 1, True, False)

screen game:
    on "show" action Show("countdown_timer")
    image "bedroom"

    ## Create a grid for the buttons to appear upon.
    grid int(buttons/2) 2:
        xspacing 100
        yspacing 20
        anchor(0.5, 0.5)
        align(0.5, 0.85)
        for i in range(buttons):
            imagebutton idle "button-%s.png" % button_state[i] focus_mask True action Function(game_buttonpress, btn = i)

    ## Show text indicating score and time remaining.
    text "[score]" size 48 align (0.8, 0.145) text_align 0.5 anchor (0.5, 0.5)
    text "[time1]" size 48 color "#FFFFFF" align(0.8, 0.36) text_align 0.5 anchor (0.5, 0.5)

    ## For the timer to decrease time remaining by 1 each second while the game is active.
    if renpy.get_screen("countdown_timer") == None:
        if "lit" not in button_state:
            timer 0.1 action Function(light_button) repeat False
        timer 1.0 action If(time1 > 1, SetVariable("time1", time1 - 1), Show("game_over")) repeat If(time1 > 1, True, False)

## This marks the start of the game.
label start:

    ## This shows a background.
    scene parking lot

    ## These display lines of dialogue.
    m "My hands are cold."
    m "The throwaway thought shatters the rhythm of my even footsteps, the concert I’d just attended slipping my mind as I shove my icy hands into the confines of my jacket’s pockets."
    m "It hasn’t helped before, but maybe this time it can stave off the incoming attack."
    m "Each slight step resounds through the suffocating night air, the parking lot I was just standing in now distant as I make my leave."
    m "I hate the cold."
    m "No, that’s not right."
    m "I despise it with my entire being."
    m "I know what’s coming next- the chill in my heart, the lack of air, the self-hate. It stalks me, waiting for me to let my guard down so it can attack."
    m "I let myself get carried away tonight. I was careless."
    m "I dart my gaze to the night sky, attempting to find comfort in the cosmos before realising it’s a fruitless endeavour and I focus again on navigating the streets until I’m home."
    m "The cold hurts."
    m "Not like frostbite where your limbs go numb, or like a stubbed toe that radiates through my whole nervous system."
    m "It’s a sense of dread."
    m "This miasma of terror that lurks in the back of my mind and gnaws at my bones, sucking out the marrow and leaving my bones dry."
    m "Or a pit in my stomach that suddenly gives way and leaves me a hollow chassis of my former self."
    m "It’s always there, neverending, but relenting in its attacks to give me false hope."
    m "It shivers- no, it’s more than that; it convulses, desperate to satiate its hunger with each passing second, revolting inside of me and grabbing its claw around my heart to tug on each ventricle."

    scene bedroom

    m "After all of my frenzied walking and my self-distraction, I’m home, jamming the keys into the lock and opening the door, slamming it behind me as I dart inside, dread still permeating every movement."
    m "The chill continues to conquer my chest, its icy grip strangling my liver and dripping through my legs, leaving it nearly impossible for me to move any further."
    m "I struggle onwards, however, continuing in a resolved limp down the hallway as my limbs scream at me to lie down on the floor and rest, and hobble into my bedroom."
    m "It’s isolated, cut off from the rest of the world since the blinds are tightly shut, so I don’t bother with taking off my jacket as I collapse onto my sheets and curl into a ball in a forlorn attempt to disappear within the mattress."
    m "Despite my position buried within the covers, the cold continues to advance through my body, overwhelming my movement and pulsating through my skin with each heartbeat."
    m "It’s for the best that I’m living alone. Without other people, I can’t infect them with this chill- this monster, the vile creature that resides in my skin and disguises itself as a flakey excuse for a human."
    m "Maybe we’re one in the same. Maybe we were made for eachother."
    m "Maybe I’m doomed to keep feeding this creature, and it’s born to keep draining me no matter what I do to fight back."
    m "We’ll always reincarnate, be reborn in one another’s presence just to keep this terrible cycle from hurting other people."
    m "I’d be okay with it, in that case."
    m "Saving other people from this terrifying thing would make me feel better when I deal with it, at least."
    m "My heartbeat surges -- it’s an agonising, tumultuous pain that radiates through my nerves and forces me to clutch at my cranium."
    m "I would do anything to get rid of this anguish."
    m "I need to distract myself."
    m "Maybe if I stare at the wall for long enough, my pain will cease to exist, and I’ll be left in my room again."
    m "That’s only if my eyes would focus for long enough to pinpoint a specific spot, but instead they swim, and my vision continues to swirl with it, like water down a drainage pipe."
    m "Nothing ever goes right when I want it to."
    m "…"
    m "My heart hurts…"
    m "It’s sudden, unexpected, and the pain shouldn’t be anything to cry over, yet the soft sting that emanates through my chest pricks tears in the corners of my eyes."
    m "It feels like something’s snapped."
    m "I’m being dramatic, I’m sure, but it still feels like an artery’s been torn apart."
    m "A strange pattern of iridescent dots dances across my vision, moving with my eyes and unavoidable while my heart continues to throb."

    ## Sets up the game and displays the screen.
    $setup_game()
    call screen game
    return



    ## This ends the game.
    return
