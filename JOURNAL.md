# June 4: Working on the cad.
I spent a lot of time today getting the geometry of the gimbal put together. I knew that I would need some sort of thrust bearing, and a way of putting all of the load of the turret assmebly onto that bearing. I ended up using a strategy of sandwhiching the bearings together.
This sandwhiching meant that no matter how load was applied to the bearing, it would always go into the main thrust bearing instead of anything else, which would make a very rigid and reliable pan joint.

<img width="1576" height="2094" alt="image" src="https://github.com/user-attachments/assets/60ac8db7-74d4-4e76-95c2-677168971b81" />

You can see in the image here, its simply a thrust bearing with a screw in the middle on the base. This will make more sense when the rest is more built.

<img width="1576" height="2094" alt="image" src="https://github.com/user-attachments/assets/c827b78f-1fb8-4c6e-a4e2-91a2f497912d" />

The load here is entirely on that thrust bearing, with two thrust bearings on either side of the bolt holting it in to ensure that it continous to rotate fully freely regardless of what direction or kind of load is put on the platform.

<img width="1576" height="2094" alt="image" src="https://github.com/user-attachments/assets/59ae4b1f-f3a2-49a0-8e32-6c39fdbcaaa5" />

Here I am brainstorming ideas on how I could build that arms that go up. I end up realizing this wide sqaure collides with the drive motor for the pan that isnt modeled in right now.

<img width="1576" height="2094" alt="image" src="https://github.com/user-attachments/assets/57fa54b0-d866-4d31-a521-0dc78a94a0ad" />

I brought in my cad of the turret, with some basic offset extruded cubes and lofts to represent how the wrist element will look in the design. It should be noted that this is not how the cannon is going to look, this is 6 in to 4 in pvc, when the cannon is 4 in to 2 in. Also, it is going to be design for things other than just a cannon.

<img width="1576" height="2094" alt="image" src="https://github.com/user-attachments/assets/a1091773-f24e-47c9-9c54-9818896a975e" />

This is an early draft of the new version I am going to be actually implementing. You can see there is one base element with the drive pulley that everything is sitting on. It then attaches to two detachable arm elements that are going to hold up the steppers and the rest of the turret.

<img width="1576" height="2094" alt="image" src="https://github.com/user-attachments/assets/6222d813-feae-47f7-8d1e-981435bba8fc" />

Here is a section analysis I sent to a friend explaining my design of the bearing, You can see the larger bearing that all of the load is being placed on, as well as the bolt going through it with the two other smaller thrust bearings keeping the rigidity of that joint well.

<img width="2752" height="2072" alt="image" src="https://github.com/user-attachments/assets/76a54ac1-1cf0-4c5b-8e07-d19f22507504" />

Here you can see roughly where I ended. I did end up putting some flanges on the shafts of the motors that will be actuaing the tilt of the cannon/payload in the future. The load will be directly applied to the output shafts of the motors, however, its less load esimated then what I saw in the 3d printer that they were taken from.

I spent all day from ~1 pm to about ~2 am working on this project, im omitting roughly the amount of time where I wasnt actively doing cad/only staring at the screen figuring out how to do something.

** Total time spent: 8.6 hours **

# June 5:
Today is the day I actually remembered that I need to jounrnal. Yesterday's journals were written today, with the images I sent to my friend on Discord. That friend was over today, and kept me motivated and helped me fix the design for the rest of geometry mockup of the project. **I am only logging the time I put in today before he arrived, or what I put in while he was here. His worked is NOT logged as mine**

<img width="741" height="656" alt="{12CD24D2-11A8-425E-81FC-AC176E9FD33C}" src="https://github.com/user-attachments/assets/dbb1689c-e0f1-4875-ab76-82c4cc85c9b5" />
<img width="972" height="664" alt="{08C7C380-E61E-42E8-B887-73224CB8F9A9}" src="https://github.com/user-attachments/assets/879bea3a-ca4f-449b-bb2e-7bae52add944" />


This is the final cad that we arrived on today. You can see that there is a generic payload mount, and there is a rough model of what a zip tie based attachment for a potato cannon might look like. The zip ties is to make it easy to remove the potato cannon for further improvements (possibly replacing the hair spray based system with pneumatics) as well as being able to use the cannon alone.

Soon after finishing this design. I pitched it to my father for possbile further support in funding, however, he disliked the cannon idea due to the danger, so this project will not be used for a potato cannon anymore. The design of an easily adaptable payload will prove helpful.

Time was also spent today figuring out how a pneumatic firing would work, we spent a couple hours searching existing designs and realiaed the only way we could achieve such a design was with a solenoid value. They only make solenoid valves for small (small, 1/2 inch) pipes unlike our 2 inch firing pipe. We expiremented with having a segment of 1 inch pipe that we could adapt to the solenoid valve, but we realized it would restrict the flow too much and is simply too complicated to work reliably. We also would need to store air in the larger compartment and we were very woried about that assembly exploding with the pressure required to launch the potato.

We also spent about an hour sourcing all of the parts needed to put together this project, going to all of the cheapest places that we could think of. We planned to go to home depot for the cannon materials before that was scrapped, so we were able to remove the arc generator and pvc material that were listed. This took about 40 usd of our total. All other materials were still required. All of the electrics, pulleys and flanges that were in the model are sourced cheapely from amazon, and the 7/16ths bolts for the lengths and ammounts we needed were actually cheapest from McMaster, which is a rare occurance. Overal the parts list without the canon amounts to about 162 dollars. We will need to work more for this funding.

The design is taking advantage of several components that are already available from a decomissioned cr20 pro we got from a friend. The steppers, power supply, raspberry pi, are available. I also have some 6mm gt2 timing belt from another project that we can use for the pan axis, as the model in cad uses it for a lowered ratio and easier actuation.

BOM:
https://docs.google.com/document/d/13_K_9BwoxUnn-ND7bYpN881mAYJAPF880q18yzIybXw/edit?usp=sharing

The filament on there is an estimate for the iterations needed to get thsi project to move reliably. Its quite large, about 250x250 mm for the base and it will be taking full advantage of that size to adapt to larger payloads in the future (e.g. yagi antennas or something idk).

I need to fix several of the models (like the arms and the wrist part) to be more easily printed, as right now they are all hollow and impractical to put supports inside of, so I will split them apart and fasten them together in some method, likely m3 screws since they are already on the parts list and are easily available.

** Total Time Spent: 5.6 hours ""

# June 6: Manufacturability
I am spending today making sure that all of the parts in the design are easily printable with the materials that I have.

<img width="315" height="272" alt="{84A86445-6A24-493F-8E4F-33F0F91A468B}" src="https://github.com/user-attachments/assets/370b5609-f7b1-4d89-9091-96098c2419a6" />

Above you are able to see the work done for the center element of the turret. I split it into two halves and added several (several for the rigidity) m3 screw points to fix the two halves together.

<img width="476" height="324" alt="{E2C26ED9-06B3-45D8-9B5E-A8A21FC8A49A}" src="https://github.com/user-attachments/assets/f9c279c4-a965-43e3-98f3-21ecf55c6486" />

The intention is to print it in this orientation, with tree supports going up to support the screw holes. This fixes the problem before where there was large cavities in these parts that were impossible to print because you cant remove supports from them, and not having supports just wouldn't work on me or my friend's printers. (mine is snapmaker a350, his ender 3 v2, both meh printers compared to a bambu)

I am going to continue working on this, adding screws to the appropriate lengths, verifying tolerances, and then doing the same for the arm assemblies. Hopefully I can keep those identical so the files stay the same, other than a left and right version of them for printing.

<img width="543" height="329" alt="{8547E2E8-D016-4EF7-9B4E-318C335343D5}" src="https://github.com/user-attachments/assets/533465d3-29d9-4c6a-a06a-6e524e759cd8" />

Now all the screws are put in place. Above is what it looks like now.

<img width="563" height="296" alt="{DCD7BBF9-5F9B-41F5-918E-DBF829EBC35A}" src="https://github.com/user-attachments/assets/9f8c52a3-63cd-4e7b-8796-13bcb0a4f098" />
<img width="154" height="40" alt="{74F02BAC-A1C1-4202-B171-741E0885B517}" src="https://github.com/user-attachments/assets/037fe596-d482-4a92-86e8-a78514151f47" />
<img width="188" height="44" alt="{20C95B25-2388-4199-91FA-5655854A429B}" src="https://github.com/user-attachments/assets/5831144c-f4d3-4b75-804a-c2a481c6bbd7" />

Above is the new arm design, there are two seperate models since this one could not simply be flipped around like the other one, it had to be actually mirrored since its not symetric on that axis. I will now assembly it back into the main design, almost all of the joins are broken so I will delete and redo the top half of the turret in the main assembly for that.

<img width="345" height="301" alt="{72665906-90F0-47E8-8DB7-2520E02BC878}" src="https://github.com/user-attachments/assets/96ac68a7-65c2-43b2-895b-0c882c2e650f" />
<img width="296" height="235" alt="{D8DE048A-3025-4200-A3A4-52B7ED1DF960}" src="https://github.com/user-attachments/assets/6fff044d-7887-49f8-b7b9-b19f40040eea" />

Above you are able to see what the new full assembly is looking like.

<img width="292" height="225" alt="{B28E8F57-4B07-4C34-807B-87B31B2321DB}" src="https://github.com/user-attachments/assets/fde47a65-57fe-49f4-a4d8-bb69f10fed57" />
<img width="406" height="208" alt="{05549D3E-0A6F-4EC1-B0DC-5525B9C09E4B}" src="https://github.com/user-attachments/assets/6a166792-bccb-4489-964c-fce3939424b3" />

I fixed the fillets on the screw holes for both of the models.

<img width="223" height="212" alt="{ACE0F1C9-FE56-4CE5-AC6E-F00398BDCB2A}" src="https://github.com/user-attachments/assets/64ae7ba6-50a5-4633-9970-f3669dfd9b00" />

The smaller inside u was limited to being only 4 mm, thats because of the face you see above. The arms are 7.5mm radius on the fillets, but the ones for the center u are only 4.

<img width="372" height="353" alt="{D2906C6E-7620-4179-91A3-5773D95EE3D0}" src="https://github.com/user-attachments/assets/da50139d-be2a-481a-8717-090bff30983b" />
<img width="240" height="166" alt="{856D74C0-98F6-4C01-9C2F-BFD9C98CC4D5}" src="https://github.com/user-attachments/assets/b93046ea-9672-4e3d-8058-c1b04870d9c1" />
<img width="324" height="272" alt="{DFD8472D-B1A9-49D4-8ADF-0C27886A4A51}" src="https://github.com/user-attachments/assets/afce3a52-dbcc-4c43-ac97-e33a1702038e" />


I realized that the motor sticking out was sort of optional, so I decided in favor of using a little less filament to move it in like you see here.

<img width="369" height="111" alt="{35516E54-B6FD-4C0E-BD6D-D6E2F74AFDF5}" src="https://github.com/user-attachments/assets/f014063e-b142-4f42-a617-c7c768914264" />

I had to increase the height of the feet for the motor to not be clipping into the ground. This is because the motor was lowered to the height of the bottom of the platform, both to make printing a little easier but also do make the shaft not clip into the arm while it rotated.

<img width="444" height="352" alt="{9C6506C7-CD5B-4DB5-82B6-6C8F6E4AE5F0}" src="https://github.com/user-attachments/assets/cfc14764-9659-4997-bc41-4831274e56fb" />

Here is what the updated model is looking like with the potato cannon payload. I think that I will next work on covers for the side motor arm things.

I updated the BOM and found cheaper sourcing then McMasterCarr for the bolts (being Bolt Depot, they look pretty trustworthy and the entire cost WITH SHIPPING is less than the cart on mcmaster without.)

Again, here is that BOM:

https://docs.google.com/document/d/13_K_9BwoxUnn-ND7bYpN881mAYJAPF880q18yzIybXw/edit?usp=sharing

I will continue to reduce the amazon cost what I can, but I will need about 5.1 more hours to get the funding required to build this project.

<img width="215" height="127" alt="{6D8C674E-2109-44D0-B431-AE065116E4EB}" src="https://github.com/user-attachments/assets/e7e4a238-728a-4a19-9996-da72ce2930cc" />

<img width="958" height="347" alt="{46A1C294-DED1-4B96-8726-D10BE9B9392B}" src="https://github.com/user-attachments/assets/c16b89f4-426f-4361-beb3-a6427376f2a4" />

As you can see, my amazon is tweaking. I am still trying to optimize the parts list a little more. I noticed that the thrust bearings were entered wrong, and I am going to have to change them. I also noticed I still had the unused limit switches listed, so I will be removing those as I found the ones that were part of the cr20 and I will plan to use those instead.

I got amazon to work on my thinkpad, idk why my framework wouldnt load the product information. Anyway, I removed the limit switches, removed the drive pulley since I found one with the belt that would work, and fixed the bearings. I will now recalculate the totals.

The other two things that I thought I would be able to cut some cost with were the c13 power connectors and the output flanges for the stepper motors. The flanges were 2x6.99, but I found the same thing but a two pack for 1x 6.99 (I didnt look very hard initially, that came back to bite me of course). The footprint appears super similar, so I wont have to modify the design from my understanding. I will now resum, hopefully we are less overbudget :pray:
It looks to be about a 13 dollar reduction in cost! I will recalculate the tax and see how far over we still are.

<img width="131" height="24" alt="{52462BDD-EF0E-4F46-B97A-9C71E3CCECD3}" src="https://github.com/user-attachments/assets/4acdaec4-27e0-4625-be1d-0ff8d9cba25e" />

These are the new totals! (Including tax!!) This is much better than the previous.

** Total time spent: 5.4 hours **
