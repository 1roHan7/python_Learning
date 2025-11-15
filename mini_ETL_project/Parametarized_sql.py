Insert_query = """
CREATE TABLE world_cup_summary (
    year INT,
    host_country VARCHAR(100),
    winner VARCHAR(100),
    runners_up VARCHAR(100),
    third VARCHAR(100),
    fourth VARCHAR(100),
    goals_scored FLOAT,
    qualified_teams INT,
    matches_played INT
);
"""