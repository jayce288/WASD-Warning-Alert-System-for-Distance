import folium

latitude = 35.1531
longitude = 128.1011

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
              color='tomato',
              radius=50,
              tooltip='경상대학교').add_to(m)

m.save('map.html')


