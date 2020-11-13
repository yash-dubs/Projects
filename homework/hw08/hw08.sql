CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT d.name, s.size
  FROM dogs AS d, parents AS p, sizes AS s
  WHERE d.height > s.min AND d.height <= s.max
  GROUP BY d.name;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT p.child
  FROM dogs AS d, parents AS p
  WHERE p.parent = d.name
  ORDER BY d.height DESC;
  
  
  
  
  ;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT p1.child AS kid, p2.child AS infant
  FROM parents AS p1, parents AS p2
  WHERE p1.child > p2.child AND p1.parent = p2.parent
  
  
  ;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT s2.infant || " and " || s2.kid || " are " || s.size || " siblings"
  FROM size_of_dogs AS s, size_of_dogs AS s1, siblings AS s2
  WHERE s2.kid = s.name AND s2.infant = s1.name AND s.size = s1.size
  
  
  ;


-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height, n);
INSERT INTO stacks_helper
  SELECT d.name, d.height, d.height, 1
  FROM dogs AS d;
INSERT INTO stacks_helper
  SELECT st.dogs || ", " || d.name, st.stack_height + d.height, d.height, 2
  FROM stacks_helper AS st, dogs AS d 
  WHERE st.last_height < d.height;
INSERT INTO stacks_helper
  SELECT st.dogs || ", " || d.name, st.stack_height + d.height, d.height, 3
  FROM stacks_helper AS st, dogs AS d 
  WHERE st.last_height < d.height;
INSERT INTO stacks_helper
  SELECT st.dogs || ", " || d.name, st.stack_height + d.height, d.height, 4
  FROM stacks_helper AS st, dogs AS d 
  WHERE st.last_height < d.height;


CREATE TABLE stacks AS
  SELECT dogs, stack_height 
  FROM stacks_helper 
  WHERE stack_height >= 170 
  ORDER BY stack_height;

