CREATE VIEW IF NOT EXISTS usa_sightings (sighted, reported, shape, state)
AS SELECT t1.sighted, t1.reported, t1.shape, t2.full_name
FROM ufodata t1 JOIN states t2
ON (lower(t2.abbreviation) = lower(substr( t1.sighting_location, -3, 2))) ;
