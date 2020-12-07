def average_age(group):
    """Compute the average age of the group's members."""
    all_ages = [person["age"] for person in group.values()]
    return sum(all_ages) / len(group)

def forget(group, person1, person2):
    """Remove the connection between two people."""
    group[person1]["relations"].pop(person2, None)
    group[person2]["relations"].pop(person1, None)


def add_person(group, name, age, job, relations):
    """Add a new person with the given characteristics to the group."""
    new_person = {
        "age": age,
        "job": job,
        "relations": relations
    }
    group[name] = new_person


if __name__ == "__main__":

    sample_dict = {}

    john_relations = {
    "Jill": "partner"
    }

    add_person(sample_dict,"John", 27, "writer", john_relations)      
    

    zalika_relations = {
    "Jill": "friend"
    }

    add_person(sample_dict,"Zalika", 28, "artist", zalika_relations)   


    jill_relations = {
    "Zalika": "friend",
    "John": "partner"
    }

    add_person(sample_dict,"Jill", 26, "biologist", jill_relations)  

    
    nash_relations = {
    "John": "cousin",
    "Zalika": "landlord"
    }

    add_person(sample_dict,"Nash", 34, "chef", nash_relations)

    forget(sample_dict, "Nash", "John")


    assert len(sample_dict) == 4, "Group should have 4 members"
    assert average_age(sample_dict) == 28.75, "Average age of the group is incorrect!"
    assert len(sample_dict["Nash"]["relations"]) == 1, "Nash should only have one relation"
    print("All assertions have passed!")
