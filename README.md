# ImageAugmentation
  1. Read image from Batch folder
  2. Crop 1 batch into 16 card images
  3. Save into OriginalImages
  4. Do transformation of cards to simulate card defects
  5. Save into different 4 defection folders (Centering/Corners/Edges/Surface)
  
  
# Naming Convention
## Pokemon
Oringinal image:<br /> 
[Card type]\_[Index]\_[Frontside(F)/Backside(B)]\_[Card no.]\_[Total Card no.]\_[Card Rarity]\_[Eng/Chi/Jp].jpg<br />
E.g. PKM_001F_24_202_U_Eng.jpg<br />
<img src="https://tcg.pokemon.com/assets/img/expansions/sword-shield/cards/en-us/SWSH1_24-2x.jpg" width="200" /><br />
Energy card: [Card type]\_[Index][Frontside(F)/Backside(B)]\_[Gold/Not Gold(G/NG)][Energy Type(Fire/Water/...)]\_[Eng/Chi/Jp].jpg'<br />
E.g. PKM_002F_GFire_Eng<br />
<img src="https://i.pinimg.com/564x/e4/37/98/e43798bece19e574fda364d212b8f269.jpg" width="200" /><br />
## YuGiOh
TBD
## Magic the Gathering
TBD
