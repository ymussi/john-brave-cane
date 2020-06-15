from brave_cane.api.partner.controller import PartnerManager

class PartnerResolvers:

    def pdv_resolver_get_by_id(self, id):
        pdv = PartnerManager().get_by_id(id)
        return pdv

    def pdv_resolver_get_by_coordinates(self, lat, lng):
        pdv = PartnerManager().get_by_coordinates(lat, lng)
        return pdv
    
    def pdv_resolver_save_pdv(self, id, tradingName, ownerName, 
                         document, coverageArea, address):
        
        pdv = {
            "pdvs": [
                {
                    "id": id,
                    "tradingName": tradingName,
                    "ownerName": ownerName,
                    "document": document,
                    "coverageArea": coverageArea,
                    "address": address
                }
            ]
        }
        
        return PartnerManager().save(pdv)