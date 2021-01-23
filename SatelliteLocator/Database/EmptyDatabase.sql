CREATE TABLE SAT (catalog_number INTEGER NOT NULL PRIMARY KEY, classification CHAR, launch_year INTEGER, launch_num_and_designator VARCHAR(20));
CREATE TABLE LOC (loc_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT , sat_id INTEGER NOT NULL, date DATETIME, first_deriv_mean FLOAT, second_deriv_mean FLOAT, 
                 drag_term FLOAT, elem_set_number INTEGER, inclination FLOAT, right_asc FLOAT, eccentricity FLOAT, arg_perigree FLOAT, 
                 mean_anomaly FLOAT, mean_motion FLOAT, rev_number_at_epoch INTEGER, FOREIGN KEY (sat_id) REFERENCES SAT (catalog_number));