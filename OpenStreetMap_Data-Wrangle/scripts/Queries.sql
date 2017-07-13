-- Returns the number of nodes
SELECT count(id) as node_count
FROM nodes;

-- Returns the number of ways
SELECT count(id) as ways_count
FROM ways;

-- Counts Postal Codes
SELECT tags.value, COUNT(*) as count 
FROM (SELECT * FROM nodes_tags 
	  UNION ALL 
      SELECT * FROM ways_tags) AS tags
WHERE tags.key='postcode'
GROUP BY tags.value
ORDER BY count DESC;

-- Sorts Cities By Counts
SELECT tags.value, COUNT(*) as count 
FROM (SELECT * FROM nodes_tags UNION ALL 
      SELECT * FROM ways_tags) AS tags
WHERE tags.key LIKE '%city'
GROUP BY tags.value
ORDER BY count DESC;

-- Number of Unique Users
SELECT COUNT(DISTINCT(e.uid))          
FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways) e;

-- Top 10 Contributing Users
SELECT e.user, COUNT(*) as num
FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e
GROUP BY e.user
ORDER BY num DESC
LIMIT 10;

-- Number of Users Appearing Only Once
SELECT COUNT(*) 
FROM (SELECT e.user, COUNT(*) as num
     	FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e
     	GROUP BY e.user
     	HAVING num=1) AS u;

-- Top 10 Appearing Amenities
SELECT value, COUNT(*) AS num
FROM nodes_tags
WHERE key='amenity'
GROUP BY value
ORDER BY num DESC
LIMIT 10;

-- Most Practiced Religion
SELECT nodes_tags.value, COUNT(*) as num
FROM nodes_tags 
    JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value='place_of_worship') i
    ON nodes_tags.id=i.id
WHERE nodes_tags.key='religion'
GROUP BY nodes_tags.value
ORDER BY num DESC
LIMIT 1;

-- Most Popular Cuisines
SELECT nodes_tags.value, COUNT(*) as num
FROM nodes_tags 
    JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value='restaurant') i
    ON nodes_tags.id=i.id
WHERE nodes_tags.key='cuisine'
GROUP BY nodes_tags.value
ORDER BY num DESC;