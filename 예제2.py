import folium

latitude = 35.154201
longitude = 128.093055
latitude2 = 35.1531
longitude2 = 128.1011
rad = 100x

location_data = [[latitude,longitude],
                 [latitude2,longitude2]]


m = folium.Map(location=[latitude, longitude],
               zoom_start=17,
               width=1420,
               height=800)

folium.Marker([latitude, longitude],
              popup="경상대학교 가좌캠퍼스",
              tooltip="경상대학교",
              icon=folium.Icon('red', icon='star'),
              ).add_to(m)

folium.Circle([latitude, longitude],
              color='red',
              radius=rad*0.7,
              tooltip='경상대학교').add_to(m)

folium.Circle([latitude, longitude],
              color='green',
              radius=rad*0.8,
              tooltip='경상대학교').add_to(m)

folium.Circle([latitude, longitude],
              color='blue',
              radius=rad*0.9,
              tooltip='경상대학교').add_to(m)

folium.PolyLine(locations=location_data,tooltip='polyline').add_to(m)

m.save('map2.html')