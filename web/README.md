# Data
A set of APIs for use by dashboard for displaying data.

## API
### /aggs  or /filters
Returns the possible filters that are available.
<details><summary>Possible parameters:</summary>

* **filter**: will update the count on all other variables.
	possible filter params:
	* Category
	* Discount
	* Style
	* Brand
	* Size
	* Retailer
	* Colour
	* Market
	* Sex 

```
?filter={"Brand":["ZALORA"]}
```

<details>
<summary> Full api return:</summary>

```python
 {
  "Brand": {
    "& Seven Days": 32,
    .... 
    "1028": 24, 
    "youme&hunny": 19, 
    "zatu emerald": 17, 
    "zaxy": 26
  }, 
  "Category": {
    "Accessories": 68975, 
    .... 
    "Swimwear & Beachwear": 34239, 
    "Tops": 161380
  }, 
  "Colour": {
    " apricot": 43, 
    " apricot black": 3, 
    .... 
	"zinfandel": 56, 
    "zinfandel marle": 5, 
    "zinfandel wash": 6
  }, 
  "Discount": {
    .... 
    "91.0": 39, 
    "95.0": 99, 
    "96.0": 10, 
    "97.0": 1
  }, 
  "Market": {
    "Malaysia": 170800, 
    "Singapore": 170800, 
    "UK": 170800, 
    "US": 170800
  }, 
  "Retailer": {
    "adidas": 1733, 
    .... 
    "whitesoot": 624, 
    "zalora": 220454
  }, 
  "Sex": {
    "Female": 12345, 
    "Male": 0, 
    "Unisex": 124
  }, 
  "Size": {
    "CHEST 38IN R": 1,
    .... 
    "CUP A": 9, 
    "CUP B": 9, 
    "CUP C": 8  
  }, 
  "Style": {
    "A Line Dresses": 138, 
    "Backpacks": 8017, 
    .... 
    "Baju Kurungs": 6307, 
      }
}
```
</details>
</details>

### /datehist
<details><summary>Possible parameters:</summary>
eg.

```filter={"Brand":["ZALORA","ASOS"]}&groupby={"Brand":[]}&interval=quarter```
* **filter**: will only return results that are in the filters
	possible filter params:
	* Category
	* Discount
	* Style
	* Brand
	* Size
	* Retailer
	* Colour
	* Market
	* Sex 
* **groupby**: will add groupings for categories same options as filters, but no additional values required
* **interval**: the date groupings that you want can be 'quarter', 'year', 'month', 'week', 'day' can also be '14d' for 14 days,'360h' for 360 hours
<details>
<summary> Full api return:</summary>

```python
{
  "Brand": {
    "ASOS": [
      1622, 
      1774, 
      2699, 
      13959, 
      23422, 
      7165, 
      5946, 
      2032
    ], 
    "ZALORA": [
      35, 
      339, 
      1332, 
      2190, 
      1785, 
      1672, 
      4871, 
      1153
    ]
  }, 
  "Count": [
    1657, 
    2113, 
    4031, 
    16149, 
    25207, 
    8837, 
    10817, 
    3185
  ], 
  "x-axis": [
    "2015-07-01T00:00:00.000Z", 
    "2015-10-01T00:00:00.000Z", 
    "2016-01-01T00:00:00.000Z", 
    "2016-04-01T00:00:00.000Z", 
    "2016-07-01T00:00:00.000Z", 
    "2016-10-01T00:00:00.000Z", 
    "2017-01-01T00:00:00.000Z", 
    "2017-04-01T00:00:00.000Z"
  ]
}
```
</details>
</details>

### /numberhist
Numberhist is for returning buckets based on numeric terms eg. Price, Discount%, DiscountPrice, OriginalPrice

<details><summary>Possible parameters:</summary>
eg.

```filter={"Brand":["ZALORA","ASOS"]}&groupby={"Brand":[]}&interval=10&dimension=Price```
* **filter**: will only return results that are in the filters
	possible filter params:
	* Category
	* Discount
	* Style
	* Brand
	* Size
	* Retailer
	* Colour
	* Market
	* Sex 
* **groupby**: will add groupings for categories same options as filters, but no additional values required
* **interval**: the date groupings that you want can be 'quarter', 'year', 'month', 'week', 'day' can also be '14d' for 14 days,'360h' for 360 hours
* **dimension**: the x-axis dimension

<details>
<summary> Full api return:</summary>

```python
{
  "Brand": {
    "ASOS": [
      55335, 
      2992, 
      193, 
      68, 
      23, 
      7, 
      1
    ], 
    "ZALORA": [
      13377, 
      0, 
      0, 
      0, 
      0, 
      0, 
      0
    ]
  }, 
  "Count": [
    68712, 
    2992, 
    193, 
    68, 
    23, 
    7, 
    1
  ], 
  "x-axis": [
    0.0, 
    300.0, 
    600.0, 
    900.0, 
    1200.0, 
    1500.0, 
    1800.0
  ]
}```
</details>
</details>

### /termhist
Term hist is for returning buckets based on terms eg. Styles

<details><summary>Possible parameters:</summary>
eg.

```filter={"brand":["ZALORA"]}&dimension=Style&groupby={"brand":["ZALORA"]}```
* **filter**: will only return results that are in the filters
	possible filter params:
	* Category
	* Discount
	* Style
	* Brand
	* Size
	* Retailer
	* Colour
	* Market
	* Sex 
* **groupby**: will add groupings for categories same options as filters, but no additional values required
* **interval**: the bucket size desired, 10,20,30 - currently this is in RM for Price, and 1,2,3 in % for Discount
* **dimension**: the x-axis dimension

<details>
<summary> Full api return:</summary>

```python
{
  "Brand": {
    "ZALORA": [
      0, 
      1756, 
      1156, 
      865, 
      776, 
      719, 
      719, 
      491, 
      411, 
      358
    ]
  }, 
  "Count": [
    3315, 
    1756, 
    1156, 
    865, 
    776, 
    719, 
    719, 
    491, 
    411, 
    358
  ], 
  "x-axis": [
    "*", 
    "Sandals", 
    "Flats", 
    "Swing Dresses", 
    "Mini Dresses", 
    "High Heels", 
    "Mid Heels", 
    "Shift Dresses", 
    "Lace Dresses", 
    "Shirts & Blouses"
  ]
}
```
</details>
</details>

### /trends
Return the top 12 ( may become more ) trends

<details>
<summary>Possible parameters:</summary>
eg. NO FILTERS ARE ACTIVE YET - API IS SERVING MOCK DATA

```filter={"Market":["UK"],"Gender":["female"] }}```
* **filter**: will only return results that are in the filters
	possible filter params:
	* Category ( later )
	* Retailer ( later )
	* Market ( later )
	* Gender  (later )
	* Date (later )
	* PriceRange (later)

<details>
<summary> Full api return:</summary>

```python
{"trends":[{"index chart":{"x-axis":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119],"score":[37.64052345967664,24.001572083672234,29.787379841057395,42.40893199201458,38.675579901499677,10.22722120123589,29.500884175255896,18.486427917023023,18.96781148206442,24.105985019383725,21.440435711608779,34.54273506962975,27.610377251469936,21.216750164928287,24.438632327454259,23.33674327374267,34.94079073157606,17.948417362341993,23.130677016509016,11.459042606982753,-5.529898158340785,26.536185954403608,28.644361988595059,12.57834979593558,42.697546239876078,5.456343254012353,20.45758517301446,18.128161499741667,35.327792143584577,34.69358769900285,21.549474256969164,23.781625196021737,11.122142523698873,0.19203531776073036,16.520878506738474,21.563489691039803,32.30290680727721,32.02379848784411,16.126731825920478,16.976972494246647,9.514470349329074,5.799820628210249,2.937298093749874,39.5077539523179,14.903478182483465,15.619256983888136,7.472046399500737,27.7749035583191,3.8610215244204868,17.872597197860313,11.045334388063245,23.86902497859262,14.891948624311269,8.193678158775878,19.71817771661345,24.283318705304177,20.66517222383168,23.024718977397816,13.656779063190364,16.37258834012862,13.27539552224049,16.404468384594588,11.86853717955546,2.7371739766832308,21.774261422537529,15.98219063791738,3.6980165303395546,24.627822555257745,10.927016356167578,20.51945395796139,27.29090562177537,21.289829107574108,31.394006845433006,7.651741796463474,24.02341641177549,13.151899090596868,11.292028508181183,14.211503352355845,16.884474678726276,20.561653422297455,8.348501592166436,29.008264869541873,24.656624397304598,4.637563137227762,34.882521937956,38.95889176030583,31.78779571159651,18.20075164187649,9.292473784894576,30.544517269311368,15.968230530268205,32.224450703824278,22.0827497807686,29.76639036483713,23.56366397174402,27.06573168191948,20.105000207208204,37.858704939058359,21.269120927036199,24.019893634447017,38.83150697056254,6.522409388575536,7.295150015142664,29.693967081580113,8.268765948858402,39.436211856492928,15.863810192402527,12.525451885592423,39.22942026480385,34.805147914344249,38.675589604265699,29.060446582753856,11.387743149452975,39.10064953099034,17.319966290486197,28.024563957963954,29.47251967773748,18.449899069091658,26.1407937034608,29.222066715665269]},"image":"http://lp2.hm.com/hmprod?set=source[/environment/2016/8AZ_0095_002R.jpg],width[3789],height[4431],x[792],y[90],type[FASHION_FRONT]&hmver=0&call=url[file:/product/main]","change":20,"gender":"female","name":"Bomber Jacket"},{"index chart":{"x-axis":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119],"score":[36.24345363663242,13.882435863499247,14.718282477365444,9.270313778438295,28.654076293246786,-3.015386968802826,37.4481176421648,12.387930991048972,23.190390960570988,17.506296245225898,34.62107937044974,-0.6014070949765404,16.775827959864928,16.159456453315845,31.337694423354376,9.001087326859692,18.27571792449564,11.221415820786282,20.422137467155929,25.82815213715822,8.993808227870787,31.44723709839614,29.015907205927957,25.02494338901868,29.008559492644119,13.162721408256669,18.771097744813518,10.642305657409314,17.32111920373984,25.30355466738186,13.083392482746909,16.032464731440226,13.128272998804006,11.547943585012805,13.28753869163181,19.873354010810986,8.826896513647223,22.344156978170923,36.5980217710987,27.420441605773357,18.08164447638385,11.123710359151638,12.528417062491624,36.92454601027747,20.50807754776029,13.630043534306467,21.90915484667466,41.002551364788427,21.201589524816293,26.172031097074194,23.001703199558276,16.477501535064815,8.574818019778599,16.506572775871225,17.91105766625222,25.866231911821978,28.38983413874505,29.311020813035574,22.855873252542588,28.85141164270728,12.456020590033472,32.52868155233288,25.12929820418009,17.019071648972845,24.88518146537497,19.244282869789445,31.31629387451427,35.19816816422199,41.85575406533161,6.035036645118623,5.5588619457041059,14.955341370535488,21.600370694478305,28.76168921116225,23.156349472416055,-0.2220121582400303,16.93795987371628,28.279746426072465,22.300947353643836,27.620111803120247,17.776718573896408,17.992419310700027,21.865613909882844,24.100516472082565,21.982997201267698,21.19008645807459,13.293377137109694,23.775637863209196,21.21821270991437,31.294839079119197,31.989178799015073,21.85156417483944,16.247150499098859,13.612695925457777,24.23494354064113,20.773400683485595,16.561463244289244,20.43596856834247,13.799991560518708,26.980320340722188,15.528714352140018,32.24507704805499,24.034916417908,25.93578523237067,9.050881542589583,21.69382433058668,27.405564510962749,10.462993981920654,17.337814939963779,20.326145466933587,6.2688267975324429,23.15159392042292,28.461606475850336,11.404840591680136,23.505459786641074,6.877165887625683,19.61304490733949,3.8422764529670525,31.214177082356643,24.089005379368279]},"image":"http://static.my.zalora.net/p/something-borrowed-5177-6366521-1.jpg","change":45,"gender":"female","name":"Mini Skirts"},{"index chart":{"x-axis":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119],"score":[15.832421525945293,19.437331727736706,-1.3619609566845413,36.40270808404989,2.065644148051369,11.58252634343796,25.02881417158043,7.5471191339276839,9.42047781137661,10.909923850731506,25.51454044546424,42.922080128149577,20.415393929984036,8.820745548864832,25.39058320580789,14.038403001935329,19.808695034788486,31.75001219500291,12.521290507061377,20.09025250973325,11.21892106759658,18.435658296153766,22.565704520012959,10.112209512303782,16.611780339708039,17.638159691473989,13.623449875156988,8.123877136147158,5.7878277269587319,18.46504804323051,17.309430397839866,42.31366788886604,-4.34767576521044,21.12726504816649,23.704445366632343,33.59633862672596,25.018572067813133,11.557862961701382,20.000097614715963,25.423525721490294,16.864918030065913,27.710117380694116,1.319093454362367,37.31184665980468,34.676780105734128,16.643226614761525,26.113407795737176,20.479705918681885,11.708647109852212,20.877102184083314,30.00365886550695,16.1890748248465,16.243305769210065,19.25529237106019,24.334963300765709,32.78379230271868,13.653206948206377,25.08396242683432,22.16116006263682,1.4138761387650263,15.806835178473112,18.676711015632568,19.604297603063946,23.260034333869809,-0.4032304872871535,20.462555231416969,13.223244226719585,5.605609732613818,25.242964300103489,27.352795760652027,13.467497322079645,28.4245628157134,16.18483518234914,20.664890091461449,9.012610530039435,35.84487056395676,-6.594494563834882,19.08547377109342,26.951196050469915,-0.3346654612261375,18.105307352876193,19.227813346470428,28.247030054369817,32.48212920597034,15.961077306620606,6.154813334641352,33.67235423927124,32.17885633056291,15.379946518466195,23.508884940877466,23.81866234126697,25.662754414424563,22.04207978914112,34.066962416613709,2.620404956154321,30.408239533907289,23.804719702150004,17.828647312551206,31.735314984949534,-3.4360319099996206,31.61521490740773,23.860780476035946,8.668667263230175,24.33092554656691,16.959135611986846,45.8529486806455,38.35332722864825,24.406898724151099,12.807461585733228,14.165854054209924,16.74950371618214,14.397654937622029,10.977539319294982,14.090277245305547,17.238205077492624,14.831161062674133,13.014100500636113,10.711080754761808,45.504382358796608,5.268267522001144]},"image":"http://www.forever21.com/images/1_front_750/00098304-01.jpg","change":-45,"gender":"female","name":"Sports Leggings"}]}
```
</details>
</details>

### /trenddetails
Return the top 12 ( may become more ) trends

<details>
<summary>Possible parameters:</summary>
eg. NO FILTERS ARE ACTIVE YET - API IS SERVING MOCK DATA

```trend=Mini Skirts```
* **filter**: will only return results that are in the filters
	possible filter params:
	* Category ( later )
	* Retailer ( later )
	* Market ( later )
	* Gender  (later )
	* Date (later )
	* PriceRange (later)

<details>
<summary> Full api return:</summary>

```python
{"activity chart":{"x-axis":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119],"In Stock":[61,69,40,58,19,18,75,93,60,27,80,2,72,32,31,55,22,98,59,79,30,98,2,22,87,72,48,2,40,72,76,1,28,65,80,92,59,23,63,16,61,81,69,32,16,22,55,30,56,12,16,58,86,61,0,18,7,26,73,30,30,3,95,36,50,46,5,53,31,99,31,6,35,81,80,66,25,64,53,2,69,46,82,28,59,3,72,68,76,14,82,99,47,35,87,92,57,67,89,6,38,23,31,22,69,29,81,7,92,73,69,20,21,55,9,20,23,63,97,31],"Out of Stock":[75,30,3,32,95,61,85,35,68,15,65,14,53,57,72,87,46,8,53,12,34,24,12,17,68,30,56,14,36,31,86,36,57,61,79,17,6,42,11,8,49,77,75,63,42,54,16,24,95,63,98,22,27,32,16,75,58,60,54,96,70,32,16,59,92,55,88,5,81,93,79,67,55,60,57,83,27,78,18,87,55,20,9,9,73,27,57,50,7,57,78,68,23,75,41,39,70,2,71,70,27,47,54,93,19,6,48,14,60,55,52,51,37,42,7,19,21,85,55,14]},"index chart":{"x-axis":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119],"score":[20.26374772849562,22.60321701422651,16.048544584822069,17.95699094961738,7.283673452805974,-5.9687863025701379,22.896809118505467,11.266953561877728,23.940726565612829,29.3510554388491,19.84315292444013,22.59595966253331,5.2668575890975799,28.01926596076254,2.492476133284807,15.049480685756134,9.913991906768855,20.25244185874402,18.784931453186866,4.531268180799859,13.930560264603555,6.06187327644048,13.723045054385473,23.32632154355982,4.586331581534214,36.70299820371597,15.004541346886829,26.73128964566061,42.48089573181875,3.457372489507577,15.256029838267257,16.980847590993429,10.689736229124943,31.109860596933737,18.10317041553862,32.784095909934247,14.459228810435976,23.543027399926364,15.597238276660442,15.75551172711949,22.280816248514485,25.790441669573519,11.458116467993495,11.5865966644753,13.442958878027039,18.53117298450079,5.880244990491526,17.294431754448,31.293033044967474,6.597419284238162,17.50703971741721,37.63492212545458,14.080405731608213,10.921883187826298,22.717996173869037,19.95438329429447,28.54106936278775,4.099951160727722,20.560489869110758,21.05862566516008,19.091624223535857,12.8612394397374,22.03715393901839,32.030318374220289,20.843130685233935,21.639339233420935,23.737515499731914,17.730931497197977,13.287255954124604,23.14109879425017,34.844181130943429,26.52164157993826,17.674266324169286,31.847461865596963,29.209473120192397,32.16500788676572,1.167371947928185,22.212919773365426,38.16595254595013,37.428839750766368,19.395222125709389,14.104521518904978,11.779704073467963,19.477818428984717,19.147625314083709,24.310528283825467,18.033204405268273,13.394085876637075,17.535033554829427,17.9045719624159,14.937889903674846,5.613788042545904,17.959890040833657,14.32565612783399,16.512210640305154,9.698117671670829,25.85846256826165,23.718297405469014,-4.071454677207814,29.639831517430843,20.965040941376786,24.287660268578695,25.973336484846358,27.300863716909384,8.085391838498876,35.145775113220839,13.023556634582347,16.737606302216798,27.83164836122184,3.128752643180384,34.16410810491588,13.708452884886328,14.838036314964837,44.46593268322016,4.1779935278059459,1.9436411511736225,23.779993001585927,9.764138196819692,10.42023520677109,17.989293493470965]},"image":"http://static.my.zalora.net/p/something-borrowed-5177-6366521-1.jpg","change":45,"gender":"female","name":"Mini Skirts"}
```
</details>
</details>

### /productdetail
Return the details for a single product UniqueKey

<details>
<summary>Possible parameters:</summary>
```id=UniqueKey```

<details>
<summary> Full api return:</summary>
{
  "_id": "MY/zalora/IC626AC02PIFSG", 
  "_index": "14082017retailer", 
  "_score": null, 
  "_source": {
    "AU size": [
      "*"
    ], 
    "Brand": "ICE-WATCH", 
    "CountryRetailer": "MY/zalora", 
    "EU size": [
      "*"
    ], 
    "IT size": [
      "*"
    ], 
    "RU size": [
      "*"
    ], 
    "UK size": [
      "*"
    ], 
    "US size": [
      "*"
    ], 
    "UniqueKey": "MY/zalora/IC626AC02PIFSG", 
    "age": 367, 
    "attributes": [
      "brand detail encapsulated"
    ], 
    "beautyscore": 1.0, 
    "brand": "Ice-Watch", 
    "brandscore": 9, 
    "clothing": "Accessories", 
    "color": "white/rose gold", 
    "colorarraytext": [
      "red", 
      "white", 
      "yellow"
    ], 
    "country": "MY", 
    "currency": "MYR", 
    "date": "2016-08-07", 
    "description": "Add a touch of elegance to your casual look with this Glam timeteller by Ice Watch. Equipped with sleek aesthetics, its colour contrast hands and brand detail are encapsulated in a sturdy silicone case.\n\n- Silicone case\n- Silicone strap\n- Colour contrast bezel\n- Debossed notches display on dial\n- 3 hands Japanese movement\n- Water resistant 10 ATM\n- Adjustable pin buckle fastening\n\nColour: White/Rose Gold\n\nMeasurements\n Face Length x Height\n- 4cm x 4cm \n\nReturns Policy :\n- Enjoy the flexibility of our 30-day free returns policy!\n- Simply pack the item, with its original packaging and tags, and the returns slip into the ZALORA delivery package. Then drop the package off at your nearest POSLAJU outlet!\n- Have a question? Please feel free to get in touch with our friendly Customer Experience Team at customer@my.zalora.com, or call us at +603-2035 6622 daily, 9am - 6pm.\n", 
    "discount_currency": "MYR", 
    "discount_pct": 0, 
    "discount_price": "", 
    "id": "MY/zalora/IC626AC02PIFSG", 
    "images": [
      "http://static.my.zalora.net/p/ice-watch-6908-768285-1.jpg", 
      "http://static.my.zalora.net/p/ice-watch-4735-768285-2.jpg", 
      "http://static.my.zalora.net/p/ice-watch-4735-768285-3.jpg", 
      "http://static.my.zalora.net/p/ice-watch-4736-768285-4.jpg"
    ], 
    "in_stock": true, 
    "name": "Ice Glam Unisex Watch", 
    "occasion": [
      "*"
    ], 
    "onlineretailername": "zalora", 
    "original_price": 399.0, 
    "price": 399.0, 
    "retailer_facet": "zalora", 
    "searchtext": " ice glam unisex watch watches & timepieces ", 
    "sizes": [
      "ONE SIZE"
    ], 
    "slug": "accessories-watches-timepieces", 
    "style": [
      "watches & timepieces"
    ], 
    "sub_sub_type": [
      "Watches & Timepieces"
    ], 
    "sub_type": [
      "*"
    ], 
    "subcolors": [
      "red", 
      "white", 
      "yellow"
    ], 
    "subtype": "watches & timepieces", 
    "topcolors": [
      "red", 
      "white", 
      "yellow"
    ], 
    "type": "accessories", 
    "updated": 1502637058, 
    "url": "https://www.zalora.com.my/ice-watch-ice-glam-unisex-watch-white-582867.html"
  }, 
  "_type": "product", 
  "sort": [
    1502637058000
  ], 
  "time_series_data": {
    "discounted_dates": [], 
    "first_date": "2017-08-04 14:46:07.875000+00:00", 
    "last_date": "2017-08-15 14:27:08.525000+00:00", 
    "price_date_ranges": [
      {
	"advertising_price": "399.00", 
	"end_date": "2017-08-16 03:56:54.454976+00:00", 
	"selling_price": "399.00", 
	"start_date": "2017-08-04 14:46:07.875000+00:00"
      }
    ], 
    "sellout_dates": []
  }
}
</details>
</details>

### /colour
Return the colour aggregates grouped by color names according to the ISCC–NBS naming system.
Also returns average hex value over all product colors with the same color name.

<details>
<summary>Possible parameters:</summary>

	possible filter params:
	* Category ( later )
	* Retailer ( later )
	* Market ( later )
	* Gender  (later )
	* Date (later )
	* PriceRange (later)

<details>
<summary> Full api return:</summary>
{"x-axis":["black","white","purplish white","purplish black","pinkish white","brownish pink","bluish white","pale yellowish pink","brownish black","light yellowish brown","dark grayish brown","blackish blue","grayish yellowish pink","vivid red","reddish black","dark purplish blue","grayish reddish orange","bluish black","pale pink","light purplish gray","dark grayish blue","blackish purple","light brown","light gray","vivid yellowish pink","dark yellowish pink","grayish purplish blue","pale blue","pinkish gray","light bluish gray","vivid reddish orange","moderate pink","strong red","dark gray","light grayish yellowish brown","light reddish brown","olive black","deep red","moderate blue","purplish gray","pale purplish blue","yellowish white","moderate brown","very pale blue","vivid purplish red","dark grayish reddish brown","dark grayish purple","dark red","dark grayish yellowish brown","grayish pink","light yellowish pink","medium gray","very pale purplish blue","yellowish gray","moderate orange","dark purplish gray","grayish blue","pale orange yellow","light pink","grayish yellowish brown","strong purplish blue","dark reddish brown","brownish orange","strong reddish orange","deep pink","brownish gray","moderate reddish brown","pale purplish pink","light grayish red","deep reddish orange","bluish gray","moderate yellowish pink","vivid purplish blue","moderate purplish blue","light orange","grayish olive","deep purplish blue","very pale purple","deep blue","dark grayish red","grayish reddish brown","grayish brown","dark bluish gray","moderate yellowish brown","dark blue","light blue","reddish gray","blackish red","dark reddish orange","dark grayish olive green","moderate reddish orange","grayish purple","moderate red","very deep red","very light purplish blue","strong pink","olive gray","dark yellowish brown","dark grayish green","light purplish blue","very light greenish blue","light greenish gray","deep reddish brown","dark brown","pale purple","greenish white","light brownish gray","grayish purplish pink","very pale violet","light purplish pink","grayish yellow","strong yellow","strong brown","light grayish reddish brown","grayish red","moderate orange yellow","deep purplish pink","dark pink","strong reddish brown","light yellow","strong yellowish pink","pale yellow green","dark purplish red","light grayish brown","deep brown","strong purplish pink","brilliant yellow","light olive gray","very light blue","grayish green","grayish violet","greenish black","light grayish olive","pale green","very pale green","brilliant blue","dark reddish gray","moderate purplish pink","strong blue","strong purplish red","light grayish purplish red","very light bluish green","very dark green","very dark red","moderate yellow","dark orange yellow","dark grayish olive","pale yellow","strong orange yellow","grayish olive green","dark olive","brilliant purplish blue","dark olive brown","brilliant orange yellow","light greenish yellow","dark greenish blue","very light purple","brilliant bluish green","dark violet","pale greenish yellow","vivid pink","moderate greenish blue","light greenish blue","blackish green","dark purplish pink","deep purplish red","moderate bluish green","dark green","light bluish green","brilliant green","strong violet","pale violet","greenish gray","deep orange yellow","dark grayish yellow","grayish purplish red","very dark greenish blue","dark reddish purple","dark bluish green","vivid yellow","moderate purplish red","brilliant greenish yellow","deep yellowish brown","strong orange","deep orange","brilliant greenish blue","dark purple","light orange yellow","light purple","pale reddish purple","deep yellowish pink","strong green","strong reddish purple","deep greenish blue","vivid blue","grayish yellow green","dark greenish gray","vivid green","brilliant orange","moderate green","moderate greenish yellow","vivid bluish green","grayish greenish yellow","light yellow green","light violet","vivid violet","deep purple","vivid greenish blue","dark yellow","brilliant yellow green","vivid reddish purple","deep yellow","grayish reddish purple","moderate olive brown","strong greenish blue","brilliant purple","deep bluish green","moderate violet","vivid purple","strong greenish yellow","light reddish purple","very dark purple","very light green","deep reddish purple","brilliant purplish pink","vivid greenish yellow","dark yellowish green","strong yellowish brown","vivid yellowish green","deep green","dark olive green","vivid orange","light green","very deep purplish red","moderate purple","moderate reddish purple","strong bluish green","very dark reddish purple","brilliant yellowish green","light yellowish green","moderate yellowish green","very dark bluish green","very light violet","brilliant violet","light olive","vivid orange yellow","very deep purple","strong yellowish green","moderate olive","very dark purplish red","strong purple","moderate olive green","deep violet","moderate yellow green","strong yellow green","very deep reddish purple","dark greenish yellow","light olive brown","deep yellowish green","very dark yellowish green","very deep yellowish green","very light yellowish green","deep yellow green","vivid yellow green","deep olive green"],"Hex":["#1f1d1d","#f3f2f2","#dededf","#211e22","#e6e2de","#d1ad96","#e8e8eb","#e5cdbc","#261f1c","#d09d7b","#383331","#2b2c36","#d1b1a5","#d22533","#282122","#252841","#b87a5d","#27282c","#e1d2cf","#c1bdc2","#3a3e48","#23202d","#b38364","#b6b5b2","#e5af95","#cb917c","#404c68","#96a5b4","#c7bbb5","#b7bfc5","#e63624","#daa599","#bf3b46","#545253","#b79982","#b18571","#282620","#861e2b","#4e6d93","#908b90","#7e8fa9","#ece4d3","#744f3b","#c0d3e3","#de3d78","#402e2d","#423c48","#6e2b32","#493e36","#c4aead","#e9bcb6","#7f7d7c","#bac6dd","#c7bdaa","#d48e60","#5e595f","#5a6b80","#ebc39c","#edc8c2","#7c6a59","#3253a7","#431d20","#b06b3f","#e55b45","#e96d76","#4f4848","#7a4538","#e7cad2","#b38f87","#b02d22","#80868e","#d5a7a9","#25328b","#3e4b7b","#e8ad81","#5f5840","#262d62","#d4cddc","#284269","#523b3c","#674a42","#645246","#555961","#856546","#243652","#779ec3","#8c7e7c","#2f1d20","#9e4a35","#343631","#c76d51","#736b77","#a84d50","#5d1524","#a8b5d7","#e99194","#58554d","#533929","#384744","#7c90bc","#9ad3de","#b6c4ba","#5f1317","#482a20","#a79ca9","#d6e6e4","#91867d","#c6a7b1","#babad1","#eab6c9","#ceb589","#d9b23d","#894d2c","#977c72","#8f5e59","#e1a750","#e86aa5","#c17f81","#8a201b","#ebd475","#f08b75","#dedab5","#642f3f","#98816d","#603623","#ea90b0","#efd152","#8a8776","#9cc1e3","#5f6e69","#494462","#1d201d","#85805f","#91a39b","#c2e1d5","#4191cc","#625352","#d99bb2","#2869ac","#ab3561","#ae868d","#8eded7","#203631","#461b28","#d0b261","#c18a3e","#373528","#ede0a9","#eaa32a","#4d5341","#474228","#5d78b9","#3b3021","#f2b947","#e7e072","#1c4d5c","#d2b6d5","#27ae9d","#2e2548","#e9e29a","#f5aeb4","#3c7385","#6aafc1","#1a2724","#c17b8c","#831f4d","#30706d","#235043","#5bb3af","#35b487","#4b428b","#958ea9","#7b8c87","#d38e25","#9d8a5c","#915e6b","#16323e","#5b3551","#1d5452","#f1c425","#a44e66","#e8df4d","#684928","#e5842b","#c26b26","#2da1b6","#4c3758","#eec578","#bb9cc8","#a9879b","#f2702a","#1f8161","#a64987","#328593","#2eafd3","#939a7d","#4c5956","#1e8e5c","#f39345","#37765f","#c1bb5c","#259189","#bbbb82","#cbdf87","#897eaf","#6456ca","#583170","#2e87a8","#ae9045","#bcda5c","#b42689","#bd9528","#7e5f74","#735a28","#1b7392","#dd94dc","#13423f","#5e497c","#a84dad","#cabc36","#b884a6","#2f1a33","#8acfb4","#772d64","#f7c7d5","#e7d824","#395f3f","#9e6820","#2db25d","#135943","#31432f","#f48413","#69a98e","#58183c","#866594","#8e5679","#13776d","#3f213a","#80cf77","#91bd8d","#628d62","#102e2f","#d5c4f2","#8075bd","#857b3d","#f6a614","#3f1d4c","#3d9751","#6d6631","#39182c","#875392","#5d693b","#2f1d58","#8a9a5c","#82ad49","#5b2252","#9d953f","#9e7620","#156434","#153a25","#05361c","#b5deae","#537b3c","#9bc526","#2c3512"],"Count":[23857,18992,15965,12339,9536,8942,7507,7421,6885,6120,6112,5925,5172,4639,4418,4283,4272,4222,3674,3435,3219,3199,3182,2905,2566,2268,2146,2113,2036,1877,1781,1733,1631,1599,1599,1584,1538,1531,1468,1441,1395,1366,1347,1347,1306,1294,1287,1233,1226,1202,1158,1148,1138,1090,1040,1008,1008,1006,976,865,849,838,828,827,810,800,794,793,738,734,719,715,696,688,687,667,664,657,624,620,608,607,604,592,579,566,555,535,530,513,511,504,499,493,491,471,461,452,431,429,424,421,419,418,413,387,378,360,358,351,345,338,336,325,320,318,317,316,314,313,313,290,284,284,283,278,266,263,263,259,254,254,252,251,250,247,246,234,233,229,226,224,223,217,209,204,197,195,195,190,186,185,185,184,174,169,161,157,157,156,156,155,149,145,145,144,129,126,126,120,120,119,117,114,113,111,111,105,104,101,100,98,95,95,94,90,87,87,85,83,80,77,76,75,75,72,70,70,68,68,68,68,67,67,64,61,60,60,58,56,54,52,52,51,51,50,50,50,49,48,44,44,44,43,41,38,37,37,36,35,34,34,33,33,32,32,32,32,29,29,27,27,26,25,25,25,24,23,22,22,21,18,17,17,13,13,12,12,11,10,7,7,6,4,1]}
</details>
</details>

### /colourgroup
Return the colour aggregates grouped by level 1 color names according to the ISCC–NBS naming system.
Also returns average hex value over all product colors with the same color name.

<details>
<summary>Possible parameters:</summary>

	possible filter params:
	* Category ( later )
	* Retailer ( later )
	* Market ( later )
	* Gender  (later )
	* Date (later )
	* PriceRange (later)

<details>
<summary> Full api return:</summary>
{"x-axis":["black","white","purplish white","purplish black","pinkish white","brownish pink","bluish white","pale yellowish pink","brownish black","light yellowish brown","dark grayish brown","blackish blue","grayish yellowish pink","vivid red","reddish black","dark purplish blue","grayish reddish orange","bluish black","pale pink","light purplish gray","dark grayish blue","blackish purple","light brown","light gray","vivid yellowish pink","dark yellowish pink","grayish purplish blue","pale blue","pinkish gray","light bluish gray","vivid reddish orange","moderate pink","strong red","dark gray","light grayish yellowish brown","light reddish brown","olive black","deep red","moderate blue","purplish gray","pale purplish blue","yellowish white","moderate brown","very pale blue","vivid purplish red","dark grayish reddish brown","dark grayish purple","dark red","dark grayish yellowish brown","grayish pink","light yellowish pink","medium gray","very pale purplish blue","yellowish gray","moderate orange","dark purplish gray","grayish blue","pale orange yellow","light pink","grayish yellowish brown","strong purplish blue","dark reddish brown","brownish orange","strong reddish orange","deep pink","brownish gray","moderate reddish brown","pale purplish pink","light grayish red","deep reddish orange","bluish gray","moderate yellowish pink","vivid purplish blue","moderate purplish blue","light orange","grayish olive","deep purplish blue","very pale purple","deep blue","dark grayish red","grayish reddish brown","grayish brown","dark bluish gray","moderate yellowish brown","dark blue","light blue","reddish gray","blackish red","dark reddish orange","dark grayish olive green","moderate reddish orange","grayish purple","moderate red","very deep red","very light purplish blue","strong pink","olive gray","dark yellowish brown","dark grayish green","light purplish blue","very light greenish blue","light greenish gray","deep reddish brown","dark brown","pale purple","greenish white","light brownish gray","grayish purplish pink","very pale violet","light purplish pink","grayish yellow","strong yellow","strong brown","light grayish reddish brown","grayish red","moderate orange yellow","deep purplish pink","dark pink","strong reddish brown","light yellow","strong yellowish pink","pale yellow green","dark purplish red","light grayish brown","deep brown","strong purplish pink","brilliant yellow","light olive gray","very light blue","grayish green","grayish violet","greenish black","light grayish olive","pale green","very pale green","brilliant blue","dark reddish gray","moderate purplish pink","strong blue","strong purplish red","light grayish purplish red","very light bluish green","very dark green","very dark red","moderate yellow","dark orange yellow","dark grayish olive","pale yellow","strong orange yellow","grayish olive green","dark olive","brilliant purplish blue","dark olive brown","brilliant orange yellow","light greenish yellow","dark greenish blue","very light purple","brilliant bluish green","dark violet","pale greenish yellow","vivid pink","moderate greenish blue","light greenish blue","blackish green","dark purplish pink","deep purplish red","moderate bluish green","dark green","light bluish green","brilliant green","strong violet","pale violet","greenish gray","deep orange yellow","dark grayish yellow","grayish purplish red","very dark greenish blue","dark reddish purple","dark bluish green","vivid yellow","moderate purplish red","brilliant greenish yellow","deep yellowish brown","strong orange","deep orange","brilliant greenish blue","dark purple","light orange yellow","light purple","pale reddish purple","deep yellowish pink","strong green","strong reddish purple","deep greenish blue","vivid blue","grayish yellow green","dark greenish gray","vivid green","brilliant orange","moderate green","moderate greenish yellow","vivid bluish green","grayish greenish yellow","light yellow green","light violet","vivid violet","deep purple","vivid greenish blue","dark yellow","brilliant yellow green","vivid reddish purple","deep yellow","grayish reddish purple","moderate olive brown","strong greenish blue","brilliant purple","deep bluish green","moderate violet","vivid purple","strong greenish yellow","light reddish purple","very dark purple","very light green","deep reddish purple","brilliant purplish pink","vivid greenish yellow","dark yellowish green","strong yellowish brown","vivid yellowish green","deep green","dark olive green","vivid orange","light green","very deep purplish red","moderate purple","moderate reddish purple","strong bluish green","very dark reddish purple","brilliant yellowish green","light yellowish green","moderate yellowish green","very dark bluish green","very light violet","brilliant violet","light olive","vivid orange yellow","very deep purple","strong yellowish green","moderate olive","very dark purplish red","strong purple","moderate olive green","deep violet","moderate yellow green","strong yellow green","very deep reddish purple","dark greenish yellow","light olive brown","deep yellowish green","very dark yellowish green","very deep yellowish green","very light yellowish green","deep yellow green","vivid yellow green","deep olive green"],"Hex":["#1f1d1d","#f3f2f2","#dededf","#211e22","#e6e2de","#d1ad96","#e8e8eb","#e5cdbc","#261f1c","#d09d7b","#383331","#2b2c36","#d1b1a5","#d22533","#282122","#252841","#b87a5d","#27282c","#e1d2cf","#c1bdc2","#3a3e48","#23202d","#b38364","#b6b5b2","#e5af95","#cb917c","#404c68","#96a5b4","#c7bbb5","#b7bfc5","#e63624","#daa599","#bf3b46","#545253","#b79982","#b18571","#282620","#861e2b","#4e6d93","#908b90","#7e8fa9","#ece4d3","#744f3b","#c0d3e3","#de3d78","#402e2d","#423c48","#6e2b32","#493e36","#c4aead","#e9bcb6","#7f7d7c","#bac6dd","#c7bdaa","#d48e60","#5e595f","#5a6b80","#ebc39c","#edc8c2","#7c6a59","#3253a7","#431d20","#b06b3f","#e55b45","#e96d76","#4f4848","#7a4538","#e7cad2","#b38f87","#b02d22","#80868e","#d5a7a9","#25328b","#3e4b7b","#e8ad81","#5f5840","#262d62","#d4cddc","#284269","#523b3c","#674a42","#645246","#555961","#856546","#243652","#779ec3","#8c7e7c","#2f1d20","#9e4a35","#343631","#c76d51","#736b77","#a84d50","#5d1524","#a8b5d7","#e99194","#58554d","#533929","#384744","#7c90bc","#9ad3de","#b6c4ba","#5f1317","#482a20","#a79ca9","#d6e6e4","#91867d","#c6a7b1","#babad1","#eab6c9","#ceb589","#d9b23d","#894d2c","#977c72","#8f5e59","#e1a750","#e86aa5","#c17f81","#8a201b","#ebd475","#f08b75","#dedab5","#642f3f","#98816d","#603623","#ea90b0","#efd152","#8a8776","#9cc1e3","#5f6e69","#494462","#1d201d","#85805f","#91a39b","#c2e1d5","#4191cc","#625352","#d99bb2","#2869ac","#ab3561","#ae868d","#8eded7","#203631","#461b28","#d0b261","#c18a3e","#373528","#ede0a9","#eaa32a","#4d5341","#474228","#5d78b9","#3b3021","#f2b947","#e7e072","#1c4d5c","#d2b6d5","#27ae9d","#2e2548","#e9e29a","#f5aeb4","#3c7385","#6aafc1","#1a2724","#c17b8c","#831f4d","#30706d","#235043","#5bb3af","#35b487","#4b428b","#958ea9","#7b8c87","#d38e25","#9d8a5c","#915e6b","#16323e","#5b3551","#1d5452","#f1c425","#a44e66","#e8df4d","#684928","#e5842b","#c26b26","#2da1b6","#4c3758","#eec578","#bb9cc8","#a9879b","#f2702a","#1f8161","#a64987","#328593","#2eafd3","#939a7d","#4c5956","#1e8e5c","#f39345","#37765f","#c1bb5c","#259189","#bbbb82","#cbdf87","#897eaf","#6456ca","#583170","#2e87a8","#ae9045","#bcda5c","#b42689","#bd9528","#7e5f74","#735a28","#1b7392","#dd94dc","#13423f","#5e497c","#a84dad","#cabc36","#b884a6","#2f1a33","#8acfb4","#772d64","#f7c7d5","#e7d824","#395f3f","#9e6820","#2db25d","#135943","#31432f","#f48413","#69a98e","#58183c","#866594","#8e5679","#13776d","#3f213a","#80cf77","#91bd8d","#628d62","#102e2f","#d5c4f2","#8075bd","#857b3d","#f6a614","#3f1d4c","#3d9751","#6d6631","#39182c","#875392","#5d693b","#2f1d58","#8a9a5c","#82ad49","#5b2252","#9d953f","#9e7620","#156434","#153a25","#05361c","#b5deae","#537b3c","#9bc526","#2c3512"],"Count":[23857,18992,15965,12339,9536,8942,7507,7421,6885,6120,6112,5925,5172,4639,4418,4283,4272,4222,3674,3435,3219,3199,3182,2905,2566,2268,2146,2113,2036,1877,1781,1733,1631,1599,1599,1584,1538,1531,1468,1441,1395,1366,1347,1347,1306,1294,1287,1233,1226,1202,1158,1148,1138,1090,1040,1008,1008,1006,976,865,849,838,828,827,810,800,794,793,738,734,719,715,696,688,687,667,664,657,624,620,608,607,604,592,579,566,555,535,530,513,511,504,499,493,491,471,461,452,431,429,424,421,419,418,413,387,378,360,358,351,345,338,336,325,320,318,317,316,314,313,313,290,284,284,283,278,266,263,263,259,254,254,252,251,250,247,246,234,233,229,226,224,223,217,209,204,197,195,195,190,186,185,185,184,174,169,161,157,157,156,156,155,149,145,145,144,129,126,126,120,120,119,117,114,113,111,111,105,104,101,100,98,95,95,94,90,87,87,85,83,80,77,76,75,75,72,70,70,68,68,68,68,67,67,64,61,60,60,58,56,54,52,52,51,51,50,50,50,49,48,44,44,44,43,41,38,37,37,36,35,34,34,33,33,32,32,32,32,29,29,27,27,26,25,25,25,24,23,22,22,21,18,17,17,13,13,12,12,11,10,7,7,6,4,1]}
</details>
</details>
