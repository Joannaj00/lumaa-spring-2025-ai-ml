# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

**Deadline**: Sunday, Feb 23th 11:59 pm PST

**Salary Expectation (Month)**: $25-30/hr or $2300/month given that I will be working 20hrs/week, but open to negotiation

---

# Perfume Recommendation System 🌸💨✨

This is a content-based perfume recommendation system that suggests fragrances based on user descriptions. It uses **TF-IDF vectorization** and **cosine similarity** to match user input with perfumes from a dataset.

---

## Dataset

The dataset used for this project is from Kaggle:  
[**Perfume Recommendation Dataset**](https://www.kaggle.com/datasets/nandini1999/perfume-recommendation-dataset). The dataset is already included in the /data folder.

The dataset contains:
- Name: The name of the perfume
- Brand: The brand of the perfume
- Description: Full description of the perfume
- Notes, Keywords of the perfume
- Image URL: The image of the perfume

---

## Setup

### **Requirements**
- Python 3.8+
- Virtual environment (recommended)

### **Install Dependencies**
1. Create a virtual environment (optional but recommended)
2. Install required packages 

```bash
pip install -r requirements.txt
```

## Running

- To start the recommendation system, simply run:

```bash
python3 main.py
```
- You’ll be prompted to enter a perfume description and how many recommendations you want. Example:

```text
Describe the type of perfume you're looking for:
> strong, independent woman in new york
How many recommendations do you want?:
> 5
```

## Sample Output

I chose not to display the similarity score to ensure a more positive user experience. Since lower scores could sometimes appear across all recommendations, showing them might discourage users or make them question the system's reliability. Instead, the focus remains on delivering the best possible matches.


```text
Top Perfume Recommendations:
--------------------------------------------------------------------------------

1. New York 5th Avenue Eau de Parfum by Fragrance du Bois

Description:  It's not easy to capture one of the most diverse, evolving and breathtaking cities in the world in one single fragrance- so Fragrance du Bois decided to make two instead, one each for the disparate but equally enchanting NYC summers and winters. New York 5th Avenue, dedicated to the magic of winter and the holidays in New York City, is a luxurious throwback to the vintage grandeur of past perfumes. Its sweet, woodsy, and opulent floral profile opens with the bright clarity of a rose top note, brightened with bergamot and leading into a marvelously classical-feeling spicy floral heart with just the right touch of musky complexity. Even as a luscious vanilla, cashmere wood, and gaiac base emerge, the multidimensional beauty of the florals linger, connecting the romance of old New York to the vibrant excitement of its future. Glamorous and enchanting, New York 5th Avenue is a fragrance for the dreamers.

Notes:  Bergamot, Rose, Caramel, Violet, Cyproil, Vanilla, Musk, Cashmere Wood, Guaiac Wood

--------------------------------------------------------------------------------

2. New York Eau de Parfum by Widian

Description:  New York City in the spring may be the most magical place in the world. For once a year, the electric bustle of the city is balanced with delightfully mild temperatures, gentle sunshine, and a fresh breeze that draws even the most cynical citydwellers out into New York's beautiful and far-flung public spaces, now teeming with the energy of new life. This is the inspiration for New York, the latest in Widian's tribute to the great cities, an explosion of bright citrus, spicy florals, and musky woodAll the energy of a New York spring is present from the very first spray, as New York bursts forth with sun-soaked notes of lemon, bergamot, and mandarin, kissed with a burst of pink pepper. The spicy, aromatic bouquet only grows richer in the romantic heart notes, as striking floral notes of lavender, geranium and rose are combined with coriander and juniper, conjuring a lusciously fresh and deeply sensual tone. And as the smooth, ambered base of tobacco, musk, and never-too-heavy vanilla emerges, you can practically feel the sun setting, and a nighttime of endless possibilities on the horizon. It's just another perfect spring day in the greatest city in the world.

Notes:  Bergamot, mandarin, lemon, pink pepper, lavender, coriander, juniper, geranium, orris, rose, akigala, jasmine, patchouli, caramel, vetiver, cypriol, white musk, white amber, vanilla, ambergris, olibanum, tonka, tobacco

--------------------------------------------------------------------------------

3. Maxed Out Parfum Extrait by 4160 Tuesdays

Description:  Inspired by the crazed youthful misadventures of perfumer Sarah McCartney's friend Maximilian Heusler, Maxed Out is a boozy, swaggering, delicious, illicit journey through the neverending nightlife of New York City. As McCartney puts it, "The kind of night out in New York you don't remember..." Don't worry, though- you don't have to have (or admit to) firsthand knowledge of that kind of experience to enjoy Maxed Out, which is as mouthwatering as it is intoxicating, as delightful as it is delirious. The coffee, vanilla and rum, in particular, leap off the skin, taking advantage of the extrait strength to blend into a delectable accord that walks the line between gourmand and narcotic and lasts all the way until the sun is rising over Queens and the bartenders are shouting for last call. Spend a night with Maxed Out. Who knows where you'll end up?

Notes:  Rum, coconut and lime, tobacco, coffee, cannabis essential oil, vintage musks, vanilla, cumin, Atlas cedar

--------------------------------------------------------------------------------

4. New York Intense Eau de Parfum by Fragrance du Bois

Description:  It's not easy to capture one of the most diverse, evolving and breathtaking cities in the world in one single fragrance- so Fragrance du Bois decided to make two instead, one each for the disparate but equally magical NYC summers and winters. New York Intense represents the vibrant summertime of NYC, irresistible and unique like the city itself. The top note is a spicy, sparkling citrus, with just a hint of floral accords- a sharper, more masculine-feeling counterpart to 5th Avenue. A balsamic and woodsy heart deepens the sensuality with olibanum, guaiac wood, clove, and immortelle, feeling rich and luxurious. A complex and powerful base featuring oud, amber, and myrrh smolders like the city at noon, albeit with the sophistication and refinement of observing Central Park from 50 stories above. Opulent, yet impeccably tasteful, New York Intense is an undeniable triumph.

Notes:  Cinnamon, Coriander, Orange, Blackberry, Bay Leaf, Rose, Olibanum, Guaiac Wood, Clove, Vanilla, Honey, Immortelle, Orchid, Vetiver, Cedarwood, Oud, Myrhh, Patchouli, Musk, Amber, Labdanum, Oakmoss

--------------------------------------------------------------------------------

5. Fleur Narcotique Eau de Parfum by Ex Nihilo

Description:  While the Left Bank gets all the traditional credit for being Paris' arts and cultural center,  everyone knows that it's the Rive Droite,  with its bustle,  style and know-how,  where the new generation is coming to life. Fleur Narcotique,  an airy,  vibrantly juicy floral designed as Ex Nihilo's "interpretation of the new Rive Droite woman, " is both sophisticated and sFleur Narcotique opens with a vital and fruit-laden set of top notes,  with bright,  energetic bergamot embracing a burst of juicy peach and exotic,  fruity lychee. In the heart,  the rich lusciousness of jasmine meets the fresh beauty of peony,  with light,  white orange blossom lending texture and depth. As Fleur Narcotique dries,  a rich but transparent base of wood,  musk and moss keeps the dreamily narcotic effect alive for hours,  keeping you sniffing again and again. The modern Rive Droite woman is a complex and sophisticated blend of substance and panache. Who doesn't want to smell like that?

Notes:  Bergamot, lychee, peach, jasmine, peony, orange blossom, wood, moss, musk

--------------------------------------------------------------------------------
```

