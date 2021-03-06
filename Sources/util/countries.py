#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Countries collections.
#
# All collections have the same fields -> (True, "es", "Spain")
#
# 1. Boolean. Means if country must be proceseed or not
# 2. ISO Code. Country ISO Code
# 3. Name. Country human readable name.
#

#
# All countries with iTunes, App Store o Mac App Store
#
AppleWorld = [
    (True, "ae", "United Arab Emirates"),
    (True, "ag", "Antigua and Barbuda"),
    (True, "ai", "Anguilla"),
    (True, "al", "Albania"),
    (True, "am", "Armenia"),
    (True, "ao", "Angola"),
    (True, "ar", "Argentina"),
    (True, "at", "Austria"),
    (True, "au", "Australia"),
    (True, "az", "Azerbaijan"),
    (True, "bb", "Barbados"),
    (True, "be", "Belgium"),
    (True, "bf", "Burkina-Faso"),
    (True, "bg", "Bulgaria"),
    (True, "bh", "Bahrain"),
    (True, "bj", "Benin"),
    (True, "bm", "Bermuda"),
    (True, "bn", "Brunei Darussalam"),
    (True, "bo", "Bolivia"),
    (True, "br", "Brazil"),
    (True, "bs", "Bahamas"),
    (True, "bt", "Bhutan"),
    (True, "bw", "Botswana"),
    (True, "by", "Belarus"),
    (True, "bz", "Belize"),
    (True, "ca", "Canada"),
    (True, "cg", "Democratic Republic of the Congo"),
    (True, "ch", "Switzerland"),
    (True, "cl", "Chile"),
    (True, "cn", "China"),
    (True, "co", "Colombia"),
    (True, "cr", "Costa Rica"),
    (True, "cv", "Cape Verde"),
    (True, "cy", "Cyprus"),
    (True, "cz", "Czech Republic"),
    (True, "de", "Germany"),
    (True, "dk", "Denmark"),
    (True, "dm", "Dominica"),
    (True, "do", "Dominican Republic"),
    (True, "dz", "Algeria"),
    (True, "ec", "Ecuador"),
    (True, "ee", "Estonia"),
    (True, "eg", "Egypt"),
    (True, "es", "Spain"),
    (True, "fi", "Finland"),
    (True, "fj", "Fiji"),
    (True, "fm", "Federated States of Micronesia"),
    (True, "fr", "France"),
    (True, "gb", "Great Britain"),
    (True, "gd", "Grenada"),
    (True, "gh", "Ghana"),
    (True, "gm", "Gambia"),
    (True, "gr", "Greece"),
    (True, "gt", "Guatemala"),
    (True, "gw", "Guinea Bissau"),
    (True, "gy", "Guyana"),
    (True, "hk", "Hong Kong"),
    (True, "hn", "Honduras"),
    (True, "hr", "Croatia"),
    (True, "hu", "Hungaria"),
    (True, "id", "Indonesia"),
    (True, "ie", "Ireland"),
    (True, "il", "Israel"),
    (True, "in", "India"),
    (True, "is", "Iceland"),
    (True, "it", "Italy"),
    (True, "jm", "Jamaica"),
    (True, "jo", "Jordan"),
    (True, "jp", "Japan"),
    (True, "ke", "Kenya"),
    (True, "kg", "Krygyzstan"),
    (True, "kh", "Cambodia"),
    (True, "kn", "Saint Kitts and Nevis"),
    (True, "kr", "South Korea"),
    (True, "kw", "Kuwait"),
    (True, "ky", "Cayman Islands"),
    (True, "kz", "Kazakhstan"),
    (True, "la", "Laos"),
    (True, "lb", "Lebanon"),
    (True, "lc", "Saint Lucia"),
    (True, "lk", "Sri Lanka"),
    (True, "lr", "Liberia"),
    (True, "lt", "Lithuania"),
    (True, "lu", "Luxembourg"),
    (True, "lv", "Latvia"),
    (True, "md", "Moldova"),
    (True, "mg", "Madagascar"),
    (True, "mk", "Macedonia"),
    (True, "ml", "Mali"),
    (True, "mn", "Mongolia"),
    (True, "mo", "Macau"),
    (True, "mr", "Mauritania"),
    (True, "ms", "Montserrat"),
    (True, "mt", "Malta"),
    (True, "mu", "Mauritius"),
    (True, "mw", "Malawi"),
    (True, "mx", "Mexico"),
    (True, "my", "Malaysia"),
    (True, "mz", "Mozambique"),
    (True, "na", "Namibia"),
    (True, "ne", "Niger"),
    (True, "ng", "Nigeria"),
    (True, "ni", "Nicaragua"),
    (True, "nl", "Netherlands"),
    (True, "np", "Nepal"),
    (True, "no", "Norway"),
    (True, "nz", "New Zealand"),
    (True, "om", "Oman"),
    (True, "pa", "Panama"),
    (True, "pe", "Peru"),
    (True, "pg", "Papua New Guinea"),
    (True, "ph", "Philippines"),
    (True, "pk", "Pakistan"),
    (True, "pl", "Poland"),
    (True, "pt", "Portugal"),
    (True, "pw", "Palau"),
    (True, "py", "Paraguay"),
    (True, "qa", "Qatar"),
    (True, "ro", "Romania"),
    (True, "ru", "Russia"),
    (True, "sa", "Saudi Arabia"),
    (True, "sb", "Soloman Islands"),
    (True, "sc", "Seychelles"),
    (True, "se", "Sweden"),
    (True, "sg", "Singapore"),
    (True, "si", "Slovenia"),
    (True, "sk", "Slovakia"),
    (True, "sl", "Sierra Leone"),
    (True, "sn", "Senegal"),
    (True, "sr", "Suriname"),
    (True, "st", "Sao Tome e Principe"),
    (True, "sv", "El Salvador"),
    (True, "sz", "Swaziland"),
    (True, "tc", "Turks and Caicos Islands"),
    (True, "td", "Chad"),
    (True, "th", "Thailand"),
    (True, "tj", "Tajikistan"),
    (True, "tm", "Turkmenistan"),
    (True, "tn", "Tunisia"),
    (True, "tr", "Turkey"),
    (True, "tt", "Republic of Trinidad and Tobago"),
    (True, "tw", "Taiwan"),
    (True, "tz", "Tanzania"),
    (True, "ua", "Ukraine"),
    (True, "ug", "Uganda"),
    (True, "us", "United States of America"),
    (True, "uy", "Uruguay"),
    (True, "uz", "Uzbekistan"),
    (True, "vc", "Saint Vincent and the Grenadines"),
    (True, "ve", "Venezuela"),
    (True, "vg", "British Virgin Islands"),
    (True, "vn", "Vietnam"),
    (True, "ye", "Yemen"),
    (True, "za", "South Africa"),
    (True, "zw", "Zimbabwe")
]

#
# Top 10 stores by revenues.
#
TopMarkets = [
    (True, "cn", "China"),
    (True, "us", "United States"),
    (True, "jp", "Japan"),
    (True, "gb", "United Kingdom"),
    (True, "au", "Australia"),
    (True, "ca", "Canada"),
    (True, "tw", "Taiwan"),
    (True, "kr", "Korea"),
    (True, "de", "Germany"),
    (True, "fr", "France"),
]