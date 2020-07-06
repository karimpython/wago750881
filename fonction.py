

def lireEntree(client,entree):

    lecture=client.read_coils(entree)
    return lecture.bits[0]