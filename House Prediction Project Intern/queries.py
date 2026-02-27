# INSIGHT 1 — WHO (customer profile)
INSIGHT_1 = """
SELECT occupation,
       COUNT(*) AS total_customers
FROM customers
GROUP BY occupation;
"""


# INSIGHT 2 — WHAT (search behavior)
INSIGHT_2 = """
SELECT property_type,
       COUNT(*) AS total_searches
FROM customer_search_history
GROUP BY property_type;
"""


# INSIGHT 3 — WHERE (location activity)
INSIGHT_3 = """
SELECT city,
       COUNT(*) AS total_visits
FROM visit_history
GROUP BY city;
"""


# INSIGHT 4 — WHICH properties perform
INSIGHT_4 = """
SELECT property_id,
       COUNT(*) AS total_contacts
FROM contact_history
GROUP BY property_id;
"""


# INSIGHT 5 — MAIN FUNNEL
INSIGHT_5 = """
SELECT
COUNT(DISTINCT s.customer_id) AS searches,
COUNT(DISTINCT w.customer_id) AS wishlists,
COUNT(DISTINCT v.customer_id) AS visits,
COUNT(DISTINCT c.customer_id) AS contacts
FROM customer_search_history s
LEFT JOIN wishlist w
ON s.customer_id = w.customer_id
LEFT JOIN visit_history v
ON s.customer_id = v.customer_id
LEFT JOIN contact_history c
ON s.customer_id = c.customer_id;
"""


# INSIGHT 6 - CITY LEVEL FUNNEL
INSIGHT_CITY_FUNNEL = """
SELECT
p.city,

-- searches are customer based (not property based)
COUNT(DISTINCT s.customer_id) AS searches,

COUNT(DISTINCT w.customer_id) AS wishlists,
COUNT(DISTINCT v.customer_id) AS visits,
COUNT(DISTINCT c.customer_id) AS contacts

FROM properties p

LEFT JOIN wishlist w
ON p.property_id = w.property_id

LEFT JOIN visit_history v
ON p.property_id = v.property_id

LEFT JOIN contact_history c
ON p.property_id = c.property_id

-- search joins through customer only
LEFT JOIN customer_search_history s
ON s.customer_id = w.customer_id

GROUP BY p.city;
"""


# INSIGHT 7 - PROPERTY TYPE FUNNEL
INSIGHT_PROPERTY_TYPE_FUNNEL = """
SELECT
p.property_type,

COUNT(DISTINCT s.customer_id) AS searches,
COUNT(DISTINCT w.customer_id) AS wishlists,
COUNT(DISTINCT v.customer_id) AS visits,
COUNT(DISTINCT c.customer_id) AS contacts

FROM properties p

LEFT JOIN wishlist w
ON p.property_id = w.property_id

LEFT JOIN visit_history v
ON p.property_id = v.property_id

LEFT JOIN contact_history c
ON p.property_id = c.property_id

-- searches linked via customer
LEFT JOIN customer_search_history s
ON s.customer_id = w.customer_id

GROUP BY p.property_type;
"""



# INSIGHT 8 - OCCUPATION FUNNEL
INSIGHT_OCCUPATION_FUNNEL = """
SELECT
c.occupation,

COUNT(DISTINCT s.customer_id) AS searches,
COUNT(DISTINCT w.customer_id) AS wishlists,
COUNT(DISTINCT v.customer_id) AS visits,
COUNT(DISTINCT ct.customer_id) AS contacts

FROM customers c

LEFT JOIN customer_search_history s
ON c.customer_id = s.customer_id

LEFT JOIN wishlist w
ON c.customer_id = w.customer_id

LEFT JOIN visit_history v
ON c.customer_id = v.customer_id

LEFT JOIN contact_history ct
ON c.customer_id = ct.customer_id

GROUP BY c.occupation;
"""