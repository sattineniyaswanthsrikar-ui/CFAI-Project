class Heuristics:

    @staticmethod
    def mrv(domains):

        selected = None

        min_size = float("inf")

        for vehicle, domain in domains.items():

            if 0 < len(domain) < min_size:

                min_size = len(domain)

                selected = vehicle

        return selected