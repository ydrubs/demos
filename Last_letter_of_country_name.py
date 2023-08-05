import string
import matplotlib.pyplot as plt

countries = "United States, Russia, Canada, China, Mexico, Brazil, Italy, United Kingdom, Australia, France, Germany, Spain, Japan, India, Egypt, Ireland, Iceland, Argentina, South Africa, Portugal, Sweden, Chile, Norway, South Korea, Finland, Turkey, North Korea, Greece, Iran, New Zealand, Poland, Iraq, Denmark, Madagascar, Peru, Switzerland, Cuba, Netherlands, Pakistan, Mongolia, Saudi Arabia, Indonesia, Colombia, Austria, Ukraine, Belgium, Niger, Thailand, Afghanistan, Vietnam, Morocco, Israel, Panama, Democratic Republic of the Congo, Uruguay, Bolivia, Sudan, Venezuela, Republic of the Congo, Kazakhstan, Philippines, Nigeria, Romania, Hungary, Paraguay, Nepal, Czech Republic, Croatia, Algeria, Syria, Libya, Estonia, Yemen, Slovakia, Kenya, Somalia, Haiti, United Arab Emirates, Latvia, Ethiopia, Lithuania, Malaysia, Jamaica, Papua New Guinea, Sri Lanka, Ecuador, Dominica, Chad, Oman, Belarus, Bulgaria, Laos, Cambodia, Albania, Jordan, Taiwan, Serbia, Luxembourg, Slovenia, Costa Rica, Bosnia and Herzegovina, Uzbekistan, Bangladesh, Tunisia, Zimbabwe, Honduras, Myanmar, Guatemala, Georgia, Ghana, Mali, Dominican Republic, Vatican City, Bahamas, Cyprus, South Sudan, North Macedonia, Turkmenistan, Nicaragua, Angola, Qatar, Singapore, Ivory Coast, Armenia, Lebanon, Belize, Tanzania, Malta, Uganda, El Salvador, Zambia, Fiji, Andorra, Guinea, Guyana, Moldova, Azerbaijan, Botswana, Monaco, Bhutan, Montenegro, Namibia, Central African Republic, Kuwait, Mozambique, Liberia, Liechtenstein, Suriname, Kosovo, Cameroon, Senegal, Rwanda, Togo, Tajikistan, Lesotho, Trinidad and Tobago, Eritrea, Kyrgyzstan, Barbados, Eswatini, San Marino, Maldives, Mauritania, Gambia, Malawi, Benin, Sierra Leone, Bahrain, Mauritius, Djibouti, Gabon, Federated States of Micronesia, Seychelles, Tonga, Brunei, Burkina Faso, Samoa, Cape Verde, Burundi, Equatorial Guinea, East Timor, Antigua and Barbuda, Solomon Islands, Saint Kitts and Nevis, Saint Lucia, Guinea-Bissau, Vanuatu, Marshall Islands, Tuvalu, Grenada, Kiribati, Saint Vincent and the Grenadines, Palau, Comoros, Nauru, São Tomé and Príncipe"

countries_list = countries.split(',')
alphabet = list(string.ascii_lowercase)
countries_spelled = []
countries_count = 0
count_lst = []
letter_to_search = 'u'

for country in range(len(countries_list)-1):
    countries_list[country] = countries_list[country].strip().lower()
    countries_spelled.append(list(countries_list[country]))


for i in alphabet:
    countries_count=0
    for letter in countries_spelled:
        # print(letter[-1])
        if letter[-1] == i:
            countries_count +=1
            # print(letter)
    count_lst.append(countries_count)
    print(i + ': ' + str(countries_count))


# print(f"There are {countries_count} countries that have {letter_to_search} as the last letter")
plt.xlabel("Last letter of countries name")
plt.ylabel("No. of countries")
plt.title("Ending letter of countries name")
plt.bar(alphabet, count_lst, color ='maroon',width = 0.6)
plt.show()