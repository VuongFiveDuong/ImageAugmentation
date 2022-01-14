# ImageAugmentation
  1. Read image from Batch folder
  2. Crop 1 batch into 16 card images
  3. Save into OriginalImages
  4. Crop and reshape the original images from 'OriginalImages' to 'CroppedImages'
  5. Do transformation of cards to simulate card defects
  6. Save into different 4 defection folders (Centering/Corners/Edges/Surface)
  
  Step 1-3:
  ```
  batch2img.py --batch_name=batch_en --side=F --language=en
  ```
  Step 4:
  ```
  crop_img.py
  ```
  Step 5:
  ```
  Task1.py --rotate=1 --shift_x_px=40 --shift_y_px=40
  ```
  The images are written in `Off-centered`.

  


# Naming Convention
## Pokemon [PKM]
### Pokemon card:<br /> 
[Card type]\_[Index]\_[Frontside(F)/Backside(B)]\_[Language].jpg<br />
E.g. *PKM_001F_en.jpg<br />*
<img src="https://tcg.pokemon.com/assets/img/expansions/sword-shield/cards/en-us/SWSH1_24-2x.jpg" width="200" /><br />

## YuGiOh [UGO]
TBD
## Magic the Gathering [MTG]
TBD<br />
## Remarks*
Check the excel file for more details
