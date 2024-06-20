###IMPLEMENTATION###

PLAN: https://docs.google.com/document/d/1g_IUKhooY1Mref8wtJ9g2a0s1FcGSfLz_TIKWA4HGP0/edit?usp=sharing


###TESTING###

Within my project, I intend to use both unit testing and implementation testing to ensure my project seemlessly flows together and works cohesively to procure a final product. I will use unit testing because it allows for me to properly test each individual module (for example, my text and image files, along with my button_state modules) properly to determine whether they function by themselves. This allows for me to provide better maintenance on specific segments of my code, as I can quickly identify which modules hold the bugs of the issue, and I can fix them. More specifically, relating to the button_state module I referenced earlier, I will be able to test whether the buttons in the minigame are able to switch their states at random without the need to press them and gain a score, have a timer, or have preamble image/text, thus allowing for a smoother development process.

I will also be utilising the integration testing approach, as it allows for me to connect the modules within my work and ensure they function properly together. Like cogs in a machine, they must all be polished separately (unit testing) before they need to be checked against one another (integration testing). For example, the button_state module is heavily reliant on the random_button_indexes and current_button_index values, which both comprise their own data and feed into the button_state module to determine which random button will be chosen to have its state switched from idle to lit. As such, integration testing allows for me to quickly ascertain where the issues within my code lie, and hat parts need to be better fused together t make a seemless project.

###MAINTENANCE CONSIDERATIONS###

Due to the nature of my project, it is likely that the project will need updates in accordance with Ren'Pys updates to its software and programming language, which means I will need to regularly check the content to ensure it is up to current standards for the service. As such, I need to heavily improve my commentation on specific segments of the code, so I don't lose my footing in future updates for the code, and I need to make sure my code is as crisp and easy-to-read as possible, so I can change and update it as easily as possible.

Two design practices I can implement to better this are continuous testing (to ensure I catch bugs early and clean up my code at the same time, making it easier to read and less likely to break in future updates to the software), and a Single Responsibility Principle (SRP) can be utilised to make sure each module only has one function, which will make it easier to identify what specific parts of the code have been impacted by the software changes, and can be quickly edited as an individual module without having to change several different parts of the project.

###SOCIAL AND ETHICAL ISSUES###

There are a couple of social issues that might arise from my game. Firstly, there is the lack of an android or mobile port for the game, which limits players to needing a mouse on their computer when porting to mobile would only require the mobile device as hardware and would increase the accessibiity of the game. Furthermore, if the buttons that need to be pressed in the minigame are too small or bunched together, they might be difficult and unappealing for users to look at, which can make the project less enjoyable overall. As such, during development, I'm going to carefully ensure that the assets for the art stand out against the background (for visibility) and are large/spread out enough that users can easily tell the difference between a "lit" button and an "idle" button, which improves enjoyment for all users without damage to the core of the project.
