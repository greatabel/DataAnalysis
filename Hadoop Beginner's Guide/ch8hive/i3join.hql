SELECT t1.sighted, t2.full_name
FROM ufodata t1 JOIN states t2
ON (lower(t2.abbreviation) = lower(substr( t1.sighting_location, -3, 2))) 
LIMIT 5 ;

-- comment :负数从最后一位开始截取
-- 语法: substr(string A, int start, int len),substring(string A, intstart, int len)
