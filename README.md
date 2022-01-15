# ImageAugmentation
  **1. Name each batch using the below naming convention in the `Batches` folder<br />**
  ```
  batch\_[Defect_type][Language][Index][Card_side].jpg
  
  *Defect_type: d0(No defect);d1(Surface);d2(Corner);d3(Edge);d4(Centering)
  *Language: en(English);cn(Chinese);jp(Japanese)
  *Index: 000~999
  *Card_side: F(Frontside);B(Backside)
  ```
  &emsp;E.g. *batch_d3en001F.jpg<br />*
  
  **2. Crop the batch into images**
  ```python
  batch2img.py --batch=batch_d3en001F
  ```
  &emsp;Images will be saved in `OriginalImages` folder<br />
  
  **3. Do transformation of cards to simulate card defects**
  ```python
  Task1.py --rotate=1 --shift_x_px=40 --shift_y_px=40
  ```
  &emsp;The images are written in `Off-centered`.

  


# Naming Convention
## Pokemon [PKM]
**Pokemon card:<br />**
[Card type]\_[Index]\_[Frontside(F)/Backside(B)]\_[Language].jpg<br />
E.g. *PKM_001F_en.jpg<br />*
<img src="https://tcg.pokemon.com/assets/img/expansions/sword-shield/cards/en-us/SWSH1_24-2x.jpg" width="200" /><br />

## YuGiOh [UGO]
TBD
## Magic the Gathering [MTG]
TBD<br />
## Remarks*
Check the excel file for more details
