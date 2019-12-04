.open --новая

-- Города
create table cities as
  select 38 as latitude, 122 as longitude, "Berkeley" as name union
  select 42,             71,               "Cambridge"        union
  select 45,             93,               "Minneapolis";

-- Родители
create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

-- Дети Abraham'а
c

-- Fillmores
select parent from parents where parent > child;

-- Арифметика

create table lift as
  select 101 as chair, 2 as single, 2 as couple union
  select 102         , 0          , 3           union
  select 103         , 4          , 1;

select chair, single + 2 * couple as total from lift;

-- Целые
create table ints as
  select "ноль" as word, 0 as one, 0 as two, 0 as four, 0 as eight union
  select "один"        , 1       , 0       , 0        , 0          union
  select "два"         , 0       , 2       , 0        , 0          union
  select "три"         , 1       , 2       , 0        , 0          union
  select "четыре"      , 0       , 0       , 4        , 0          union
  select "пять"        , 1       , 0       , 4        , 0          union
  select "шесть"       , 0       , 2       , 4        , 0          union
  select "семь"        , 1       , 2       , 4        , 0          union
  select "восемь"      , 0       , 0       , 0        , 8          union
  select "девять"      , 1       , 0       , 0        , 8;

select word, one + two + four + eight as value from ints;
select word from ints where one + two/2 + four/4 + eight/8 = 1;