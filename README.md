<p align="center">
  <img 
    src="https://github.com/user-attachments/assets/a25e681f-5559-4282-b565-6aaf46b99da1"
    alt="potatomatic-cover"
    style="max-width: 100%; height: auto;"
  />
</p>

# Potatomatic turret system
Potatomatic started as a project to move a 5.5lb potato cannon reliably on a robotic turret mechanism, and to have intelligent tracking allowing it to automatically control itself for a majority of it's operation. We then realized that its super simple to make it adaptable to anything! So in the end, this project is a robust 2 axis gimbal with a mounting solution allowing anything to be mounted easily for use in the future.

## Assembly guide
A complete guide to printing, assembly, wiring and programming can be found [here](https://docs.google.com/presentation/d/1axM6zSbhQgakMfhfwyYygMVe3PKqu1EDHwFVl_Ch5AA/edit?usp=sharing).

## Bom:
See the BOM.csv for the BOM. It includes everything you would need to build it assuming you had only filament. See the google doc below for what the HackClub funding would be spent on, as thats the materials I still need.

**If you dont have anything, use the BOM.csv**

**I will be purchasing from the google doc BOM, as it omits things I already have**

All of the sourcing and stuff was done on this google doc:
[Google Doc BOM](https://docs.google.com/document/d/13_K_9BwoxUnn-ND7bYpN881mAYJAPF880q18yzIybXw/edit?usp=sharing)
See the "sourcing" tab for the real BOM. The first page is a general list without prices or source locations. Note that prices are calculated for Utah.

## Project Cost Breakdown
**For HackClub reviewer: I will NOT be purchasing filament with the project grant. I have already printed all of the components out with my own funds using my PETG.**


### Summary

| Category | With Filament | Without Filament |
|----------|---------------|------------------|
| Total (inlc-tax) | $158.38 | $116.54 |
| Amazon Section | $123.16 (~$132.34 w/ tax) | $84.22 (~$90.50 w/ tax) |
| Bolt Depot Section | $26.04 | $26.04 |

---

## Amazon Parts

| Item | Cost |
|------|------|
| Filament | $38.94 |
| Controller (Arduino + stepper driver combo) | $17.83 |
| Stepper output flanges | $6.99 |
| DC-DC Step Down (24V → 12V) | $9.99 |
| Barrel Power Connector | $3.97 |
| Motor Cabling | $7.89 |
| C13 Socket | $5.99 |
| Thrust Bearings (2× 15×28×2mm) | $12.38 |
| Thrust Bearing (1× 80×105×4mm) | $9.19 |
| M3 Screw Set | $9.99 |

---

## Bolt Depot Parts

| Item | Cost |
|------|------|
| 4× 1.5" 7/16 Bolts | $2.72 |
| 9× 1.25" 7/16 Bolts | $5.31 |
| 13× 7/16 Nuts | $4.94 |

## 3D model
<img width="762" height="509" alt="{4FDD96C2-EDEC-4343-98A4-A21E9CE5DD90}" src="https://github.com/user-attachments/assets/fca63770-0cd5-4d77-bdb6-b2d4b8eb74ed" />

## Wiring
Below is very professional Google Slides diagram of the wiring. I omitted the pi to better fit on one slide, since its only USB connectors that can go in one place one way. Note my typo, apparently cat5a doesnt exist. I meant cat5e. I got mixed up with cat6a which I use for my homelab.

<img width="960" height="540" alt="wiring" src="https://github.com/user-attachments/assets/99866ae4-f4be-4b7a-91c1-8cd7548a10c4" />

The pi will have a webcam conencted, and serial connected to the control board. The wiring for this project is very simple, there is a limited number of electrical components other than the motors and camera and control boards. The control board does almost everything, if you look at what I linked its a steal honestly.

## Other notes:
The plan is to have entirely custom firmware for the turret, it will use a pi 5 that I already have as well as a camera attached to the turret (will have to be built before I can get a good idea of the best place) for targetting automatically. The main control will use the linked arduino stepper controller board with the pi talking to it with serial commands. There is a later intention of mounting it ontop of my friends car for some funny turret activities (dont ask) as well as adapting it for directional antennas to do radio astronomy, connecting to gpredict.
