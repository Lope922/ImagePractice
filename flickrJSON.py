import requests
from PIL import Image
import urllib
import json
import shutil


# flickr api address

#search for bird species




#fAPI_add = "".format(animal)


flickerSearchURL = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=920322c4d9cb2198bab884879c0a9546&tags=rhino&format=json&nojsoncallback=1'

        #Search flickr for cat pictures
flickrResponse = urllib.request.urlopen(flickerSearchURL)
#get json back
flickrResponseJSONString = flickrResponse.read().decode('UTF-8')
flickrResponseJson = json.loads(flickrResponseJSONString)
    #Get first json object ('photos') which contains another json object ('photo') which is an json array; each
        # element represents one photo. Take element 0
        #firstResponsePhoto = flickrResponseJson['photos']['photo'][0]

for animal in range(0, 5):
            jsonforphoto = flickrResponseJson['photos']['photo'][animal]
            #deal with this in the following way. vvvvvvv

            #Extract the secret, server, id and farm; which you need to construct another URL to request a specific photo
            #https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg

            # the the phreses we need
            secret = jsonforphoto['secret']
            id = jsonforphoto['id']
            server = jsonforphoto['server']
            farm = jsonforphoto['farm']

            print(jsonforphoto)  #Just checking we get the JSON we expect
            #TODO add error handing

            fetchPhotoURL = 'https://farm%s.staticflickr.com/%s/%s_%s_m.jpg' % (farm, server, id, secret)
            print(fetchPhotoURL)   #Again, just checking

            #Reference: http://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
            animalName = 'animal'
            animal_responseFileNameJpg = 'animal' + str(animal) + '.jpg'

            animalPicFileGif = 'animal' + str(animal) + '.gif'

            #Read the response and save it as a .jpg. Use shutil to copy the stream of bytes into a file
            #What does 'with' mean? http://preshing.com/20110920/the-python-with-statement-by-example/

            # todo NOTE that this is a stream, see if there are other ways i can utilize the stream feature to do different things.

            # this is where it actually makes the request.
            resp = requests.get(fetchPhotoURL, stream=True)

            with open(animal_responseFileNameJpg, 'wb') as out_file:
               #todo look into shutils to see what it is???  <<~~~~~~~
               # my guess is that it reads the response and turns it into the gif format as a new file save.
                shutil.copyfileobj(resp.raw, out_file)
                img = Image
                img.frombytes(mode="rb", size=500, data=out_file).show()

           # deletes the response and free up resources.
            del resp




            #TODO tweak the resutls maybe search for photos that have a lot of likes that match the animal species, also sort by interesting. ???