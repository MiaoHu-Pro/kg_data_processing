/location/location/contains(X0, X2) :- /location/location/contains(X0, X1), /education/educational_institution_campus/educational_institution(X2, X1)
/location/location/contains(X0, X2) :- /location/location/contains(X0, X1), /education/educational_institution/campuses(X2, X1)
/location/location/contains(X0, X2) :- /location/location/contains(X0, X1), /education/educational_institution_campus/educational_institution(X1, X2)
/location/location/contains(X0, X2) :- /location/location/contains(X0, X1), /education/educational_institution/campuses(X1, X2)
/location/location/contains(X0, X2) :- /dataworld/gardening_hint/split_to(X1, X0), /location/location/contains(X1, X2)
/education/educational_degree/people_with_this_degree./education/education/institution(X0, X2) :- /education/educational_degree/people_with_this_degree./education/education/institution(X0, X1), /education/educational_institution_campus/educational_institution(X2, X1)
/education/educational_degree/people_with_this_degree./education/education/institution(X0, X2) :- /education/educational_degree/people_with_this_degree./education/education/institution(X0, X1), /education/educational_institution/campuses(X2, X1)
/education/educational_degree/people_with_this_degree./education/education/institution(X0, X2) :- /education/educational_degree/people_with_this_degree./education/education/institution(X0, X1), /education/educational_institution_campus/educational_institution(X1, X2)
/education/educational_degree/people_with_this_degree./education/education/institution(X0, X2) :- /education/educational_degree/people_with_this_degree./education/education/institution(X0, X1), /education/educational_institution/campuses(X1, X2)
/education/field_of_study/students_majoring./education/education/institution(X0, X2) :- /education/field_of_study/students_majoring./education/education/institution(X0, X1), /education/educational_institution/campuses(X2, X1)
/education/field_of_study/students_majoring./education/education/institution(X0, X2) :- /education/field_of_study/students_majoring./education/education/institution(X0, X1), /education/educational_institution_campus/educational_institution(X2, X1)
/education/field_of_study/students_majoring./education/education/institution(X0, X2) :- /education/field_of_study/students_majoring./education/education/institution(X0, X1), /education/educational_institution/campuses(X1, X2)
/education/field_of_study/students_majoring./education/education/institution(X0, X2) :- /education/field_of_study/students_majoring./education/education/institution(X0, X1), /education/educational_institution_campus/educational_institution(X1, X2)
/education/educational_institution/students_graduates./education/education/major_field_of_study(X0, X2) :- /education/educational_institution/campuses(X0, X1), /education/educational_institution/students_graduates./education/education/major_field_of_study(X1, X2)
/education/educational_institution/students_graduates./education/education/major_field_of_study(X0, X2) :- /education/educational_institution_campus/educational_institution(X0, X1), /education/educational_institution/students_graduates./education/education/major_field_of_study(X1, X2)
/education/educational_institution/students_graduates./education/education/major_field_of_study(X0, X2) :- /education/educational_institution/campuses(X1, X0), /education/educational_institution/students_graduates./education/education/major_field_of_study(X1, X2)
/education/educational_institution/students_graduates./education/education/major_field_of_study(X0, X2) :- /education/educational_institution_campus/educational_institution(X1, X0), /education/educational_institution/students_graduates./education/education/major_field_of_study(X1, X2)
/people/person/profession(X0, X2) :- /people/person/profession(X0, X1), /dataworld/gardening_hint/split_to(X1, X2)
/education/educational_institution/students_graduates./education/education/student(X0, X2) :- /education/educational_institution_campus/educational_institution(X0, X1), /education/educational_institution/students_graduates./education/education/student(X1, X2)
/education/educational_institution/students_graduates./education/education/student(X0, X2) :- /education/educational_institution/campuses(X0, X1), /education/educational_institution/students_graduates./education/education/student(X1, X2)
/education/educational_institution/students_graduates./education/education/student(X0, X2) :- /education/educational_institution/campuses(X1, X0), /education/educational_institution/students_graduates./education/education/student(X1, X2)
/education/educational_institution/students_graduates./education/education/student(X0, X2) :- /education/educational_institution_campus/educational_institution(X1, X0), /education/educational_institution/students_graduates./education/education/student(X1, X2)
/people/person/places_lived./people/place_lived/location(X0, X2) :- /people/person/places_lived./people/place_lived/location(X0, X1), /location/hud_county_place/place(X2, X1)
/people/person/places_lived./people/place_lived/location(X0, X2) :- /people/person/places_lived./people/place_lived/location(X0, X1), /location/hud_county_place/place(X1, X2)
/education/educational_institution/students_graduates./education/education/degree(X0, X2) :- /education/educational_institution_campus/educational_institution(X0, X1), /education/educational_institution/students_graduates./education/education/degree(X1, X2)
/education/educational_institution/students_graduates./education/education/degree(X0, X2) :- /education/educational_institution/campuses(X0, X1), /education/educational_institution/students_graduates./education/education/degree(X1, X2)
/education/educational_institution/students_graduates./education/education/degree(X0, X2) :- /education/educational_institution_campus/educational_institution(X1, X0), /education/educational_institution/students_graduates./education/education/degree(X1, X2)
/education/educational_institution/students_graduates./education/education/degree(X0, X2) :- /education/educational_institution/campuses(X1, X0), /education/educational_institution/students_graduates./education/education/degree(X1, X2)
/location/location/containedby(X0, X2) :- /education/educational_institution_campus/educational_institution(X0, X1), /location/location/containedby(X1, X2)
/location/location/containedby(X0, X2) :- /education/educational_institution/campuses(X0, X1), /location/location/containedby(X1, X2)
/location/location/containedby(X0, X2) :- /location/location/containedby(X0, X1), /dataworld/gardening_hint/split_to(X1, X2)
/location/location/containedby(X0, X2) :- /education/educational_institution/campuses(X1, X0), /location/location/containedby(X1, X2)
/location/location/containedby(X0, X2) :- /education/educational_institution_campus/educational_institution(X1, X0), /location/location/containedby(X1, X2)
/film/film/release_date_s./film/film_regional_release_date/film_release_region(X0, X2) :- /film/film/release_date_s./film/film_regional_release_date/film_release_region(X0, X1), /dataworld/gardening_hint/split_to(X1, X2)
/people/profession/people_with_this_profession(X0, X2) :- /dataworld/gardening_hint/split_to(X1, X0), /people/profession/people_with_this_profession(X1, X2)
/film/film/country(X0, X2) :- /film/film/country(X0, X1), /dataworld/gardening_hint/split_to(X1, X2)
/people/person/education./education/education/institution(X0, X2) :- /people/person/education./education/education/institution(X0, X1), /education/educational_institution/campuses(X2, X1)
/people/person/education./education/education/institution(X0, X2) :- /people/person/education./education/education/institution(X0, X1), /education/educational_institution_campus/educational_institution(X2, X1)
/people/person/education./education/education/institution(X0, X2) :- /people/person/education./education/education/institution(X0, X1), /education/educational_institution/campuses(X1, X2)
/people/person/education./education/education/institution(X0, X2) :- /people/person/education./education/education/institution(X0, X1), /education/educational_institution_campus/educational_institution(X1, X2)
/people/person/nationality(X0, X2) :- /people/person/nationality(X0, X1), /dataworld/gardening_hint/split_to(X1, X2)