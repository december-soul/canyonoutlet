def buildUrl(args):
    website =           "https://www.canyon.com/"
    locale =            "en-%s/" % args.locale
    outlet =            "outlet/"
    bikeType =          "%s-bikes/" % args.type
    outletType =        "?cgid=outlet-%s" % args.type
    price =             "&pmax=%s" % args.max_price
    prefn1 =            "&prefn1=pc_familie"
    prefn2 =            "&prefn2=pc_geschlecht"
    prefn3 =            "&prefn3=pc_outlet"
    prefn4 =            "&prefn4=pc_rahmengroesse"
    prefn5 =            "&prefn5=pg_materialgroup"
    prefn6 =            "&prefn6=pc_schaltwerk_web_schaltwerk_model"
    prefv1 =            "&prefv1=%s" % args.model
    prefv2 =            "&prefv2=%s" % args.gender
    prefv3 =            "&prefv3=true"
    prefv4 =            "&prefv4=%s" % args.size
    prefv5 =            "&prefv5=Complete%20bikes"
    prefv6 =            "&prefv5=%s" % args.group
    sorting =           "&srule=sort_price_ascending"
    hideFilters =       "&hideSelectedFilters=true"

    url = "".join([website, 
                    locale, 
                    outlet, 
                    bikeType, 
                    outletType,
                    price,
                    prefn1,
                    prefn2,
                    prefn3,
                    prefn4,
                    prefn5,
                    prefn6,
                    prefv1,
                    prefv2,
                    prefv3,
                    prefv4,
                    prefv5,
                    prefv6,
                    sorting,
                    hideFilters
                ])
    return url
