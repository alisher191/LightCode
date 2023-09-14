--
-- PostgreSQL database dump
--

-- Dumped from database version 14.6 (Homebrew)
-- Dumped by pg_dump version 14.6 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: house; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.house (
    id integer NOT NULL,
    pub_no character varying(100) NOT NULL,
    title character varying(255) NOT NULL,
    link text NOT NULL,
    image text NOT NULL,
    description text NOT NULL,
    price character varying(255) NOT NULL,
    city character varying(100) NOT NULL,
    location character varying(255) NOT NULL,
    date_added character varying(100) NOT NULL
);


ALTER TABLE public.house OWNER TO postgres;

--
-- Name: house_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.house_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.house_id_seq OWNER TO postgres;

--
-- Name: house_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.house_id_seq OWNED BY public.house.id;


--
-- Name: person; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.person (
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    born integer NOT NULL
);


ALTER TABLE public.person OWNER TO postgres;

--
-- Name: house id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.house ALTER COLUMN id SET DEFAULT nextval('public.house_id_seq'::regclass);


--
-- Data for Name: house; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.house (id, pub_no, title, link, image, description, price, city, location, date_added) FROM stdin;
1	1	Renovated bachelor, Queen and Niagara - ID 1474	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/renovated-bachelor-queen-and-niagara-id-1474/1645234719	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/27/27794407-dda2-413d-ae1b-1ebeb840b4e4?rule=kijijica-200-jpg	Renovated Akelius studio apartment for rent. Queen & Niagara in the Downtown West neighborhood, Toronto. renovated studio - 1 bathroom - located on floor 5 - approximately 236 square feet - available ...	$1,550.00	Toronto	Niagara Street	27/12/2022
2	2	Bachelor for Rent Steps to Victoria Park Station!	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/bachelor-for-rent-steps-to-victoria-park-station/1643370118	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/74/742bb861-df40-462d-9ca7-ca7b6e5dd702?rule=kijijica-200-jpg	Touch free leasing: Virtual viewings via video conferencing and online leasing available. Book yours today. Our Rental Office remains operational in light of COVID-19. The health and safety of you, ...	$2,149.00	City of Toronto	Richmond Street West	05/01/2023
3	3	Glen Park Apartments - One Bedroom Apartment for Rent	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/glen-park-apartments-one-bedroom-apartment-for-rent/1568953096	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/b7/b7126cc8-85de-4dbf-8596-6718c5773689?rule=kijijica-200-jpg	GLEN PARK Conveniently located, steps away from hundreds of stores on Yonge Street, and easy access to transit. Glen Park is a well-maintained property with its beautiful exterior landscaping, and ...	$2,117.00	City of Toronto	Denton Avenue	22/01/2023
4	4	1 Bedroom Apartment for Rent Steps to Victoria Park Station!	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/1-bedroom-apartment-for-rent-steps-to-victoria-park-station/1623912036	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/73/73544705-67e0-43bc-8f7d-d4f2dda02e5e?rule=kijijica-200-jpg	Touch free leasing: Virtual viewings via video conferencing and online leasing available. Book yours today. Our Rental Office remains operational in light of COVID-19. The health and safety of you, ...	$2,449.00	Toronto	MacEy Avenue	30/12/2022
5	5	1BR & 2BR Brand New Condo unit w/Parking at Lakeshore & Parklawn	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/1br-2br-brand-new-condo-unit-w-parking-at-lakeshore-parklawn/1622117405	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/3a/3a6ea935-b094-4b8c-9277-923887be26a8?rule=kijijica-200-jpg	Looking for a couple/working professional to lease brand new Condo units at Parklawn & Lakeshore available immediately !! Steps to Humber Bay Shores, Metro, Gardiner Express, LCBO, Mimico GO, ...	$2,400.00	City of Toronto	Clark Avenue	15/01/2023
6	6	New Construction: 1 Bedroom Apartment FOR RENT. Downtown Toronto	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/new-construction:-1-bedroom-apartment-for-rent-downtown-toronto/1648211023	https://media.kijiji.ca/api/v1/ca-prod-fsbo-ads/images/ae/ae2c48bb-47a6-4ca1-b630-6483dcf280c4?rule=kijijica-200-jpg	New Construction: 1 Bedroom Apartment FOR RENT. Downtown Toronto Address: 520 RICHMOND STREET WEST TORONTO ON M5V 1Y4 Newly constructed brand new condominium 1 Bedroom apartment unfurnished Utilities ...	$3,000.00	Toronto	Dudley Avenue	< 3 minutes ago
7	7	Fully Upgraded 3 Bedroom Townhouse - Perfect home for families!	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/fully-upgraded-3-bedroom-townhouse-perfect-home-for-families/1620781843	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/cb/cba4481e-5485-4644-9a7e-3607f9599244?rule=kijijica-200-jpg	2029-2055 Victoria Park Ave. Victoria Park Ave. & Ellesmere Rd. Monthly rent: Starting from $3150 Parking: $130 per month/outdoor Suite Features: Large, designer open-concept kitchen with new Bosch ...	$3,150.00	City of Toronto	Denton Avenue	< 20 minutes ago
8	8	Scarborough 2 Bedroom Apartment for Rent - 1340 Danforth Road	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/scarborough-2-bedroom-apartment-for-rent-1340-danforth-road/1568954929	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/8e/8e3e4e55-83e1-4e03-b2f9-89c86b0bdcb9?rule=kijijica-200-jpg	Current Promotions View our units by clicking the virtual tour link, schedule a video tour or make an appointment for in person viewing. (647) 696-7899Virtual Open House: View our units by clicking ...	$2,084.00	Scarborough	MacEy Avenue	< 20 minutes ago
9	9	Brand New Renovated 1 Bedroom - Walk to GO Train, Lake, Parks!	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/brand-new-renovated-1-bedroom-walk-to-go-train-lake-parks/1638455666	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/cc/cc835b32-fb7a-4e5f-9b9a-532a3e8ffff3?rule=kijijica-200-jpg	90, 92 James & 25 Villa Rd. James St. & Forty Second St. Monthly rent: Starting from $2254/month Utilities: Heat included, hydro and water extra Parking: $110/month Suite Features: Thorough cleaning ...	$2,254.00	City of Toronto	Lake Shore Boulevard West	< 20 minutes ago
10	10	LARGE Renovated 1 Bedroom ~ In The Beaches!	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/large-renovated-1-bedroom-in-the-beaches/1529878252	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/50/507fd400-b490-44d6-bcd4-25ddf3694515?rule=kijijica-200-jpg	2402-2406 Queen St East,Scarborough (The Beaches) Queen St. E & Victoria Park Ave. Monthly rent: Starting from $1980/month Utilities: Heat and water included, hydro extra Parking: $118 per month ...	$1,980.00	City of Toronto	Brookers Lane	< 20 minutes ago
11	11	2 bedroom - walk to the lake, GO Train!	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/2-bedroom-walk-to-the-lake-go-train/1642716367	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/53/535f9a88-ba3b-4ccc-929b-807700ad7d95?rule=kijijica-200-jpg	90, 92 James & 25 Villa Rd. James St. & Forty Second St. Monthly rent: Starting from $2526 Utilities: Heat included, hydro and water extra Parking: $110/month To view our property from the comfort of ...	$2,526.00	Toronto	Richmond Street West	< 20 minutes ago
12	12	Downtown 1 Bedroom Apartment for Rent - 77 Wellesley Street East	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/downtown-1-bedroom-apartment-for-rent-77-wellesley-street-east/1647422000	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/44/4403c231-a163-41d6-ada9-77e63d30bb41?rule=kijijica-200-jpg	Current Promotions View our units by clicking the virtual tour link, schedule a video tour or make an appointment for in person viewing. Call: 437-218-5969Virtual Open House: View our units by ...	$2,358.00	Toronto	Maud Street	< 20 minutes ago
13	13	1 Bedroom with must see finishes ~close to public transit	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/1-bedroom-with-must-see-finishes-close-to-public-transit/1635836611	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/69/6934964d-d8f6-4ece-9c7c-ddbfd65ce68e?rule=kijijica-200-jpg	260 Gamble Avenue (East York) Donlands Avenue & Cosburn Avenue Monthly rent: Starting from $2,113/month Utilities:Heat included, hydro and water extra Parking:$100 per month/outdoor . Suite Features: ...	$2,113.00	City of Toronto	Victoria Park Avenue	< 20 minutes ago
14	14	Stunning 1 Bedroom ~ renovated with stainless steel appliances!	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/stunning-1-bedroom-renovated-with-stainless-steel-appliances/1612005720	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/c6/c604a6d0-5995-484b-bfbb-480adbd9ff6b?rule=kijijica-200-jpg	130 Gowan Avenue (East York) Cosburn Ave & Pape Ave. Monthly rent: Starting from $2,179/month Utilities: Heat and water included, hydro extra Parking: $140 per month/indoor or $100 per month/outdoor ...	$2,179.00	East York	Cassandra Boulevard	< 20 minutes ago
15	15	Warden & St Clair 1 bedroom reno suites - Pet Friendly!	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/warden-st-clair-1-bedroom-reno-suites-pet-friendly/1643140850	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/87/87eb0731-3fcc-4d38-8fbb-ec425924e243?rule=kijijica-200-jpg	50 Burnhill Rd., Scarborough Burnhill Rd. & Warden Ave. Monthly rent: Starting from $2166/month Utilities: Heat included, water and hydro extra Parking: $145 per month/indoor OR $110 per ...	$2,166.00	Scarborough	Lake Shore Boulevard West	< 20 minutes ago
16	16	Large Bachelor at Warden Station - $500GC promo available	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/large-bachelor-at-warden-station-500gc-promo-available/1640918869	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/b4/b483f24f-638a-4367-877e-6cfdcb564650?rule=kijijica-200-jpg	50 Burnhill Rd., Scarborough Burnhill Rd. & Warden Ave. Monthly rent: Starting from $1900/month Utilities: Heat included, water and hydro extra Parking: $145 per month/indoor OR $110 per ...	$1,900.00	Scarborough	Brow Drive	< 20 minutes ago
17	17	Live in The Beaches ~ Renovated Bachelor	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/live-in-the-beaches-renovated-bachelor/1505787717	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/b3/b3dbf774-46b1-41db-b451-66229357e99e?rule=kijijica-200-jpg	2367 Queen St East,Scarborough (The Beaches) Queen St. E & Victoria Park Ave Monthly rent: Starting from $1885/month Utilities: Heat included, hydro and water extra Suite Features: Thorough cleaning ...	$1,885.00	City of Toronto	Queen Street East	< 20 minutes ago
18	18	Bachelor with high end finishes ~Close to O’Connor and St. Clair	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/bachelor-with-high-end-finishes-close-to-o-connor-and-st-clair/1594815398	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/3a/3a0389e3-afbc-4fbd-8836-723385a71b11?rule=kijijica-200-jpg	5, 7 & 9 Stag Hill Drive (East York) O'Connor Dr. & St. Clair Ave E. Monthly rent: Starting from $181/month Utilities: Heat included, hydro and water extra Parking: $100 per month/outdoor Suite ...	$1,811.00	City of Toronto	Victoria Park Avenue	< 20 minutes ago
19	19	Renovated 1 Bedroom ~ Low-rise in quiet community!	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/renovated-1-bedroom-low-rise-in-quiet-community/1645423554	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/f6/f6940a54-582e-4555-aded-247357420e3a?rule=kijijica-200-jpg	338-342 Donlands Avenue (East York) O'Connor Drive & Pape Avenue Monthly rent: Starting from $1899/month Utilities: Heat included, hydro and water extra Parking: $135 per month/outdoor Suite ...	$1,899.00	East York	Lake Shore Boulevard West	< 20 minutes ago
20	20	Renovated 1 bedroom in The Beaches	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/renovated-1-bedroom-in-the-beaches/1647636745	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/5b/5b3a5784-4d13-4795-bdf8-a91038b2f784?rule=kijijica-200-jpg	3000, 3015 & 3017 Queen St. E., Scarborough (The Beaches) Queen St. E & Victoria Park Ave. Monthly rent: Starting from $1926/month Utilities: Heat and water included, hydro extra Parking: $130 per ...	$1,926.00	Toronto	Brow Drive	< 20 minutes ago
21	21	Newly renovated bachelor ~ prime location in East York!	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/newly-renovated-bachelor-prime-location-in-east-york/1635836521	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/e0/e025c635-7fc7-4db6-93b9-2042d8958c25?rule=kijijica-200-jpg	338-342 Donlands Avenue (East York) O'Connor Drive & Pape Avenue Monthly rent: Starting at $1609/month Utilities: Heat included, hydro and water extra Parking: $135 per month/outdoor Suite Features: ...	$1,609.00	East York	Church Street	< 20 minutes ago
22	22	Gorgeous 1 Bedroom in The Beaches! Pet Friendly, quiet mid-rise!	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/gorgeous-1-bedroom-in-the-beaches-pet-friendly-quiet-mid-rise/1505826705	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/87/870f8530-6961-4145-b975-b910eabc6023?rule=kijijica-200-jpg	1150 & 1200 Kingston Rd., The Beaches Victoria Park Ave. & Kingston Rd. Monthly rent: Starting from $2141/Month Utilities: Heat included, hydro and water extra Parking: $120 per month/indoor Suite ...	$2,141.00	Toronto	Wellesley Street East	< 20 minutes ago
23	23	BRAND NEW 2 Bedroom, 4 Appliances, Lots of storage! Pet Friendly	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/brand-new-2-bedroom-4-appliances-lots-of-storage-pet-friendly/1570722466	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/b1/b1b0b332-8465-4fba-bafd-052b64b4b044?rule=kijijica-200-jpg	1080 Kingston Rd., The Beaches Victoria Park Ave. & Kingston Rd. Monthly rent: Starting from $2,593 Utilities: Heat included, hydro and water extra Parking: $127 per month/indoor and $100 per ...	$2,593.00	Scarborough	Donlands Avenue	< 20 minutes ago
24	24	Scarborough 2 Bedroom Apartment for Rent - 1360 Danforth Road	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/scarborough-2-bedroom-apartment-for-rent-1360-danforth-road/1568954269	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/8a/8a125587-96a7-4e22-8e28-3012ee68dd13?rule=kijijica-200-jpg	Current Promotions View our units by clicking the virtual tour link, schedule a video tour or make an appointment for in person viewing. (647) 696-7899Virtual Open House: View our units by clicking ...	$2,044.00	Scarborough	Gamble Avenue	< 20 minutes ago
25	25	Scarborough 2 Bedroom Apartment for Rent - 1350 Danforth Road	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/scarborough-2-bedroom-apartment-for-rent-1350-danforth-road/1568954381	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/0f/0f2da1c4-2988-44d1-9f92-127896a8763e?rule=kijijica-200-jpg	Current Promotions View our units by clicking the virtual tour link, schedule a video tour or make an appointment for in person viewing. (647) 696-7899Virtual Open House: View our units by clicking ...	$2,099.00	Scarborough	Pape Avenue	< 20 minutes ago
26	26	Luxury Bachelor ~~ Mid-Rise Building in The Beaches!	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/luxury-bachelor-mid-rise-building-in-the-beaches/1647092694	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/58/5891477e-b374-4743-851f-4dde6a1e5aee?rule=kijijica-200-jpg	1150 & 1200 Kingston Rd., The Beaches Victoria Park Ave. & Kingston Rd. Monthly rent: Starting from $2001/month Utilities: Heat included, hydro and water extra Parking: $120 per month/indoor Suite ...	$2,001.00	Toronto	Gowan Avenue	< 20 minutes ago
27	27	Scarborough 1 Bedroom Apartment for Rent - 1360 Danforth Road	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/scarborough-1-bedroom-apartment-for-rent-1360-danforth-road/1631152634	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/fa/fa327939-b06b-4983-a41f-61b2f41d9fe8?rule=kijijica-200-jpg	Current Promotions View our units by clicking the virtual tour link, schedule a video tour or make an appointment for in person viewing. (647) 696-7899Virtual Open House: View our units by clicking ...	$1,780.00	Scarborough	Warden Avenue	< 20 minutes ago
28	28	Scarborough 1 Bedroom Apartment for Rent - 1350 Danforth Road	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/scarborough-1-bedroom-apartment-for-rent-1350-danforth-road/1568954539	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/f5/f5dd4690-826c-4f65-bba0-ea782f357cfd?rule=kijijica-200-jpg	Current Promotions View our units by clicking the virtual tour link, schedule a video tour or make an appointment for in person viewing. (647) 696-7899Virtual Open House: View our units by clicking ...	$1,644.00	Scarborough	MacK Avenue	< 20 minutes ago
29	29	Downtown Large 1 Bedroom Apartment for Rent - 80 Wellesley Stree	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/downtown-large-1-bedroom-apartment-for-rent-80-wellesley-stree/1647844124	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/3d/3d7a37db-b24b-43ea-b02d-667414bd13df?rule=kijijica-200-jpg	Current Promotions View our units by clicking the virtual tour link, schedule a video tour or make an appointment for in person viewing. Call now! (647) 558-2263Virtual Open House: View our units by ...	$2,375.00	Toronto	Queen Street East	< 20 minutes ago
30	30	Brand New 1 Bedroom Condo on Bloor St East by Subway Station	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/brand-new-1-bedroom-condo-on-bloor-st-east-by-subway-station/1648209066	https://media.kijiji.ca/api/v1/ca-prod-fsbo-ads/images/e4/e42dfa04-2f50-4e29-8e4a-1dc76d6dffdc?rule=kijijica-200-jpg	Brand New Bright And Spacious 1 Bedroom At The Rosedale. Located Conveniently On The Bloor Line Just Minutes Away From Yonge, Yorkville, Uoft, Rosedale, Cabbagetown And More! Luxurious Living ...	$2,230.00	Toronto	Spruce Hill Road	< 20 minutes ago
31	31	1 Bedroom Apartment - | Call now	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/1-bedroom-apartment-call-now/1647495576	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/26/2626133f-43ac-4c5b-99cd-d6a2289505ff?rule=kijijica-200-jpg	Contact Hazelview Properties today!Need easy access to life's necessities while enjoying a relaxed living environment? From schools, shopping and sporting facilities to transit options like the Allen ...	$2,099.00	Toronto	O'Connor Drive	< 23 minutes ago
32	32	girls room in scarbought	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/girls-room-in-scarbought/1648208385	https://media.kijiji.ca/api/v1/ca-prod-fsbo-ads/images/ef/ef5b6609-b216-477b-ae14-f739d71b0731?rule=kijijica-200-jpg	one first floor big room winch big window ，shared washroom with one girl ，please call 4168998556	$900.00	Toronto	Sandra Road	< 26 minutes ago
33	33	upperlevel  house  for rent long-term and short-term	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/upperlevel-house-for-rent-long-term-and-short-term/1648208362	https://media.kijiji.ca/api/v1/ca-prod-fsbo-ads/images/5f/5f9a1262-3b50-433c-9683-d1d10f61d4cd?rule=kijijica-200-jpg	2 story house for rent: -4 bedrooms -3 bathroom one en suite bathroom -separate laundry separate entrance -beautiful backyard with a deck -near Steeles and dufferin intersection in glenshield -very ...	$3,500.00	City of Toronto	Queen Street East	< 26 minutes ago
34	34	Lake Shore Blvd & Don Roadway |1 Bed+ Den 1Bath | Condo For Rent	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/lake-shore-blvd-don-roadway-1-bed-den-1bath-condo-for-rent/1648208088	https://media.kijiji.ca/api/v1/ca-prod-fsbo-ads/images/ae/aec4bc0f-71a2-47ed-9de9-0fdaf4ba7641?rule=kijijica-200-jpg	Toronto | Lake Shore Blvd W| Lake Shore Blvd & Don Roadway |1 Bed + Den| 1 Bath | Condo For Rent Spacious 1 Bedroom plus den, 1 Bathroom condo with Living & Dining Area, Big Windows with lots of ...	$3,295.00	Toronto	Courcelette Road	< 28 minutes ago
35	35	Scarborough 1B Apartment All Inclusive + 1M FREE	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/scarborough-1b-apartment-all-inclusive-1m-free/1638333516	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/3b/3b38a8b7-0274-4cdf-b6c3-b6d4e3ccdb3d?rule=kijijica-200-jpg	51 Trailridge Cres., Scarborough now offering 1 month free on 1 bedroom unit. Neilson Rd. & Ellesmere Rd. Monthly rent: starting from $2200 All Utilities included in rental price:Heat, water and ...	$2,200.00	City of Toronto	Donlands Avenue	< 32 minutes ago
36	36	Large Modern Condo For Rent 1 Bedroom Plus Den Downtown Toronto	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/large-modern-condo-for-rent-1-bedroom-plus-den-downtown-toronto/1648207329	https://media.kijiji.ca/api/v1/ca-prod-fsbo-ads/images/c7/c71df0a4-ab70-45db-a4f9-74c6aa84d9e2?rule=kijijica-200-jpg	Large Modern Condo For Rent 1 Bedroom Plus Den Downtown Toronto * Breathtaking Views Of The City Skyline * Award Winning X2 Condo By Great Gulf Home. * 9Ft Ceiling. Window. * Eat-In Island In ...	$2,750.00	Toronto	Torrens Avenue	< 35 minutes ago
37	37	High-Level 2 Bed Condo Rental in Kenndy/401	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/high-level-2-bed-condo-rental-in-kenndy-401/1648207268	https://media.kijiji.ca/api/v1/ca-prod-fsbo-ads/images/b5/b59d17e1-6fca-464d-a7c9-097fc0de8cf5?rule=kijijica-200-jpg	High-level spacious 1+1 bedroom (Den is semi-enclosed, can be used as office/kids room), 1 bathroom. Rent also includes Rogers high-speed internet and 1 parking space. 255 Village Green Square - ...	$2,500.00	Toronto	Kingston Road	< 35 minutes ago
38	38	Wellington Place, Penthouse 2 bedroom + terrace	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/wellington-place-penthouse-2-bedroom-terrace/1640981231	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/08/08d12c4e-f90b-41eb-8aeb-4d8fe967a53c?rule=kijijica-200-jpg	Penthouse suite 2 bdrm, 1 bath- 858 sq ft, corner suite with a wrap around terrace ( 702 sq ft) east and south views stainless appliances, white high gloss cabinets, quartz countertops ensuite ...	$3,695.00	City of Toronto	Courcelette Road	< 37 minutes ago
39	39	30 Edith: Apartment for rent in Toronto	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/30-edith:-apartment-for-rent-in-toronto/1647500045	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/b7/b726c2e8-9c76-4945-b82e-a6c1f81bae5b?rule=kijijica-200-jpg	30 Edith offers comfortable living in the pleasant Yonge and Eglinton Corridor of Northern Toronto. Our 1 & 2 bedroom, pet-friendly suites offer indoor and outdoor parking, along with spacious ...	$2,599.00	Toronto	Danforth Road	< 37 minutes ago
40	40	30 Edith: Apartment for rent in Toronto	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/30-edith:-apartment-for-rent-in-toronto/1647500081	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/5f/5f19e61f-c13a-4b54-bb42-7d41bb9912b4?rule=kijijica-200-jpg	30 Edith offers comfortable living in the pleasant Yonge and Eglinton Corridor of Northern Toronto. Our 1 & 2 bedroom, pet-friendly suites offer indoor and outdoor parking, along with spacious ...	$3,199.00	Toronto	Thicketwood Drive	< 37 minutes ago
41	41	Spacious 1 Bed + Den Avenue Rd & Lawrence Ave	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/spacious-1-bed-den-avenue-rd-lawrence-ave/1526047287	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/11/115e8a83-f55a-48ba-9203-d7b1fd965f75?rule=kijijica-200-jpg	Apartments at Rosewell Gardens are located at Avenue Road and Lawrence Avenue in one of the most prestigious residential and family orientated neighbourhoods in Toronto. Rosewell Gardens is also ...	$2,895.00	City of Toronto	Danforth Road	< 37 minutes ago
42	42	2 Bedroom Suite at Avenue and Lawrence	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/2-bedroom-suite-at-avenue-and-lawrence/1526079109	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/36/365ab187-03ca-4dee-a019-e29fdecaf36e?rule=kijijica-200-jpg	Apartments at Rosewell Gardens are located at Avenue Road and Lawrence Avenue in one of the most prestigious residential and family orientated neighbourhoods in Toronto. Rosewell Gardens is also ...	$3,295.00	Toronto	Thicketwood Drive	< 37 minutes ago
43	43	Large 1 bedroom basement apartment with high ceiling and granite	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/large-1-bedroom-basement-apartment-with-high-ceiling-and-granite/1648206992	https://media.kijiji.ca/api/v1/ca-prod-fsbo-ads/images/ad/ada21c22-b73a-4b7f-b5f0-0e4ac20c7d33?rule=kijijica-200-jpg	This unit is located in the Dufferin and DuPont area. Also has stainless steel appliances. A new washer dryer in unit. Looking for professional couple. Must have current credit score and referrals ...	$1,700.00	Toronto	Church Street	< 37 minutes ago
44	44	One Bedroom Apartment - 849 Broadview	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/one-bedroom-apartment-849-broadview/1641931972	https://media.kijiji.ca/api/v1/ca-prod-fsbo-ads/images/a8/a80ae9ee-9af4-4764-8f36-f1c946cd805a?rule=kijijica-200-jpg	One bedroom unit located in a unique, architecturally significant building on Broadview Avenue in the trendy and highly desirable Danforth neighbourhood; for its prime location this building is ...	$1,750.00	Toronto	Wellesley Street East	< 45 minutes ago
45	45	2 Bed, 2 Baths - Downtown Condominium Suite	https://www.kijiji.ca/v-apartments-condos/city-of-toronto/2-bed-2-baths-downtown-condominium-suite/1643567492	https://media.kijiji.ca/api/v1/ca-prod-dealer-ads/images/d2/d23852c2-4b9e-4d11-aa42-06d2c4398b89?rule=kijijica-200-jpg	A fabulous 2 bedroom remodeled suite. Convenient location. Just steps to Church Street and a quick walk to Bloor Street, fine shops, restaurants, subway, and the terrific yummy Yorkville! Live and ...	$4,200.00	Toronto	Bloor Street East	< 46 minutes ago
\.


--
-- Data for Name: person; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.person (id, name, born) FROM stdin;
1	Patrick	2009
2	Yorgos	2010
3	Noak	2004
4	Elbertine	2000
5	Wald	2006
6	Fredric	1999
7	Emiline	1995
8	Devondra	1992
9	Tildi	2003
10	Clay	2012
11	Umeko	2002
12	Germain	2011
13	Quillan	2009
14	Hamel	2007
15	Cullan	2009
16	Tonie	2012
17	Zachary	2005
18	Mag	2003
19	Andromache	2009
20	Arly	1996
21	Kippie	1984
22	Genni	2008
23	Fairlie	2007
24	Thorin	2006
25	Jewel	2008
26	Chantalle	2003
27	Katerine	2003
28	Tybie	2010
29	Guy	2011
30	Shayna	1999
\.


--
-- Name: house_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.house_id_seq', 45, true);


--
-- Name: house house_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.house
    ADD CONSTRAINT house_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

