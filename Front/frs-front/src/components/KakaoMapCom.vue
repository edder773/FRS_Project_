<template>
  <div class="map-page">
    <div class="map-box">
      <div class="kakao-filter">
    <select id="region" class="kakao-select" v-model="searchSi">
      <option value="">전체</option>
      <option v-for="si in siList" :value="si" :key="si">{{ si }}</option>
    </select>
    <select class="kakao-select" v-if="searchSi ==''" id="Gu" v-model="searchGu">
      <option value="">전체</option>
    </select>
    <select class="kakao-select" v-if="searchSi =='서울특별시 '" id="Gu" v-model="searchGu">
      <option value="">전체</option>
      <option v-for="gu in SeoulList" :value="gu" :key="gu">{{ gu }}</option>
    </select>
    <select class="kakao-select" v-if="searchSi =='부산광역시 '" id="Gu" v-model="searchGu">
      <option value="">전체</option>
      <option v-for="gu in BusanList" :value="gu" :key="gu">{{ gu }}</option>
    </select>
    <select class="kakao-select" v-if="searchSi =='대구광역시 '" id="Gu" v-model="searchGu">
      <option value="">전체</option>
      <option v-for="gu in DaeguList" :value="gu" :key="gu">{{ gu }}</option>
    </select>
    <select class="kakao-select" v-if="searchSi =='인천광역시 '" id="Gu" v-model="searchGu">
      <option value="">전체</option>
      <option v-for="gu in IncheonList" :value="gu" :key="gu">{{ gu }}</option>
    </select>
    <select class="kakao-select" v-if="searchSi =='광주광역시 '" id="Gu" v-model="searchGu">
      <option value="">전체</option>
      <option v-for="gu in GuangjuList" :value="gu" :key="gu">{{ gu }}</option>
    </select>
    <select class="kakao-select" v-if="searchSi =='대전광역시 '" id="Gu" v-model="searchGu">
      <option value="">전체</option>
      <option v-for="gu in DaejeonList" :value="gu" :key="gu">{{ gu }}</option>
    </select>
    <select class="kakao-select" v-if="searchSi =='울산광역시 '" id="Gu" v-model="searchGu">
      <option value="">전체</option>
      <option v-for="gu in UlsanList" :value="gu" :key="gu">{{ gu }}</option>
    </select>
    <select class="kakao-select" v-if="searchSi =='세종특별자치시 '" id="Gu" v-model="searchGu">
      <option value="">전체</option>
      <option v-for="gu in SejongList" :value="gu" :key="gu">{{ gu }}</option>
    </select>
    <select class="kakao-select" v-if="searchSi =='경기도 '" id="Gu" v-model="searchGu">
      <option value="">전체</option>
      <option v-for="gu in GyeongiList" :value="gu" :key="gu">{{ gu }}</option>
    </select>
    <select class="kakao-select" v-if="searchSi =='강원도 '" id="Gu" v-model="searchGu">
      <option value="">전체</option>
      <option v-for="gu in GangwonList" :value="gu" :key="gu">{{ gu }}</option>
    </select>
    <select class="kakao-select" v-if="searchSi =='충청북도 '" id="Gu" v-model="searchGu">
      <option value="">전체</option>
      <option v-for="gu in ChoongbookList" :value="gu" :key="gu">{{ gu }}</option>
    </select>
    <select class="kakao-select" v-if="searchSi =='충청남도 '" id="Gu" v-model="searchGu">
      <option value="">전체</option>
      <option v-for="gu in ChoongnamList" :value="gu" :key="gu">{{ gu }}</option>
    </select>
    <select class="kakao-select" v-if="searchSi =='전라북도 '" id="Gu" v-model="searchGu">
      <option value="">전체</option>
      <option v-for="gu in JeonbookList" :value="gu" :key="gu">{{ gu }}</option>
    </select>
    <select class="kakao-select" v-if="searchSi =='전라남도 '" id="Gu" v-model="searchGu">
      <option value="">전체</option>
      <option v-for="gu in JeonnamList" :value="gu" :key="gu">{{ gu }}</option>
    </select>
    <select class="kakao-select" v-if="searchSi =='경상북도 '" id="Gu" v-model="searchGu">
      <option value="">전체</option>
      <option v-for="gu in GyeongbookList" :value="gu" :key="gu">{{ gu }}</option>
    </select>
    <select class="kakao-select" v-if="searchSi =='경상남도 '" id="Gu" v-model="searchGu">
      <option value="">전체</option>
      <option v-for="gu in GyeongnamList" :value="gu" :key="gu">{{ gu }}</option>
    </select>
    <select class="kakao-select" v-if="searchSi =='제주특별자치도 '" id="Gu" v-model="searchGu">
      <option value="">전체</option>
      <option v-for="gu in JejuList" :value="gu" :key="gu">{{ gu }}</option>
    </select>
    <select class="kakao-select" v-model="searchBank">
      <option :value="`${this.bank}`">{{this.bank}}</option>
    </select>
    <button @click="search()">검색</button>
      </div>
    </div>
    <div id="map-comp">
    </div>
  </div>
</template>

<script>
const apiKey = process.env.VUE_APP_KAKAO_API_KEY
export default {
  name: 'KakaoMapCom',
  props: {
      bank: {
        type: String,
        required: true,
      },
    },
  data() {
    return {
      map: null,
      searchSi: '',
      searchGu: '',
      searchBank: this.bank,
      markers:[],
      siList: [
      '서울특별시 ','부산광역시 ','대구광역시 ','인천광역시 ','광주광역시 ','대전광역시 ',
      '울산광역시 ','세종특별자치시 ','경기도 ','강원도 ','충청북도 ','충청남도 ',
      '전라북도 ','전라남도 ','경상북도 ','경상남도 ','제주특별자치도 '
      ],
      SeoulList: [
      "강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구", "노원구",
       "도봉구", "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구", "성북구", "송파구", 
       "양천구", "영등포구", "용산구", "은평구", "중구", "중랑구", "종로구"
      ],
      BusanList: [
      "강서구", "금정구", "기장군", "남구", "동구", "동래구", "부산진구", "북구", "사상구", "사하구",
       "서구", "수영구", "연제구", "영도구", "중구", "해운대구"
      ],
      DaeguList:[
      "남구", "달서구", "달성군", "동구", "북구", "서구", "수성구", "중구"
      ],
      IncheonList:[
      "강화군", "계양구", "남동구", "동구", "미추홀구", "부평구", "서구", "연수구"
      ],
      GuangjuList:[
      "동구", "서구", "남구", "북구", "광산구"
      ],
      DaejeonList:[
      "동구", "중구", "서구", "유성구", "대덕구"
      ],
      UlsanList:[
      "중구", "남구", "동구", "북구"
      ],
      SejongList: [
      ''
      ],
      GyeongiList:[
      "가평군", "고양시 덕양구", "고양시 일산동구", "고양시 일산서구", "과천시", "광명시", 
      "광주시", "구리시", "군포시", "김포시", "남양주시", "동두천시", "부천시", "성남시 분당구", 
      "성남시 수정구", "성남시 중원구", "수원시 권선구", "수원시 영통구", "수원시 장안구", "수원시 팔달구",
       "시흥시", "안산시 단원구", "안산시 상록구", "안성시", "안양시 동안구", "안양시 만안구", "양주시", 
       "양평군", "여주시", "연천군", "오산시", "용인시 기흥구", "용인시 수지구", "용인시 처인구",
       "의왕시", "의정부시", "이천시", "파주시", "평택시", "포천시", "하남시", "화성시"
      ],
      GangwonList:[
      "강릉시", "고성군", "동해시", "삼척시", "속초시", "양구군", "양양군", "영월군", "원주시", "인제군",
       "정선군", "철원군", "춘천시", "태백시", "평창군", "홍천군", "화천군", "횡성군"
      ],
      ChoongbookList:[
      "괴산군", "단양군", "보은군", "영동군", "옥천군", "음성군", "제천시", "증평군", "진천군", "청원군",
       "청주시 상당구", "청주시 서원구", "청주시 청원구", "청주시 흥덕구", "충주시"
      ],
      ChoongnamList:[
      "계룡시", "공주시", "금산군", "논산시", "당진시", "보령시", "부여군", "서산시", "서천군", "아산시", 
      "예산군", "천안시 동남구", "천안시 서북구", "청양군", "태안군", "홍성군"
      ],
      JeonbookList:[
      "고창군", "군산시", "김제시", "남원시", "무주군", "부안군", "순창군", "완주군", "익산시", 
      "임실군", "장수군", "전주시 덕진구", "전주시 완산구", "정읍시", "진안군"
      ],
      JeonnamList:[
      "강진군", "고흥군", "곡성군", "광양시", "구례군", "나주시", "담양군", "목포시", 
      "무안군", "보성군", "순천시", "신안군", "여수시", "영광군",
       "영암군", "완도군", "장성군", "장흥군", "진도군", "함평군", "해남군", "화순군"
      ],
      GyeongbookList:[
      "경산시", "경주시", "고령군", "구미시", "군위군", "김천시", "문경시", "봉화군", "상주시", "성주군", "안동시", 
      "영덕군", "영양군", "영주시", "영천시", "예천군", "울릉군", "울진군", "의성군", "청도군", "청송군",
       "칠곡군", "포항시 남구", "포항시 북구"
      ],
      GyeongnamList:[
      "거제시", "거창군", "고성군", "김해시", "남해군", "밀양시", "사천시", "산청군", "양산시", "의령군", "진주시", "창녕군", "창원시 마산합포구",
      "창원시 마산회원구", "창원시 성산구", "창원시 의창구", "창원시 진해구",
       "통영시", "하동군", "함안군", "함양군", "합천군"
      ],
      JejuList:[
      "서귀포시", "제주시"
      ],

      searchdic: {
        '서울특별시 ': this.SeoulList,
        '부산광역시 ': this.BusanList,
        '대구광역시 ': this.DaeguList,
        '인천광역시 ': this.IncheonList,
        '광주광역시 ': this.GuangjuList,
        '대전광역시 ': this.DaejeonList,
        '울산광역시 ': this.UlsanList,
        '경기도 ': this.GyeongiList,
        '강원도 ': this.GangwonList,
        '충청북도 ': this.ChoongbookList,
        '충청남도 ': this.ChoongnamList,
        '전라북도 ': this.JeonbookList,
        '전라남도 ': this.JeonnamList,
        '경상북도 ': this.GyeongbookList,
        '경상남도 ': this.GyeongnamList,
        '제주특별자치도 ': this.JejuList,
      },
    }
  },

  // computed: {
  //   filteredList() {
  //     return this.searchdic[this.searchSi]
  //   },
  // },
  mounted() {
    if (!window.kakao || !window.kakao.maps) {
      const script = document.createElement("script")
      script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${apiKey}&libraries=services`
      /* global kakao */
      script.addEventListener("load", () => {
        kakao.maps.load(this.initMap)
      })
      document.head.appendChild(script)
    } else {
      this.initMap()
    }
  },
  methods: {
    initMap() {
      const container = document.getElementById("map-comp")
      const options = {
        center: new kakao.maps.LatLng(37.566826, 126.9786567),
        level: 3,
      }
      this.map = new kakao.maps.Map(container, options)
    },
    search() {
      if (this.searchBank !=='') {
        const ps = new kakao.maps.services.Places()
        ps.keywordSearch(this.searchSi+this.searchGu+this.searchBank, (data, status) => {
        if (status === kakao.maps.services.Status.OK) {
          this.clearMarkers();
          const bounds = new kakao.maps.LatLngBounds()
          
          for (let i = 0; i < data.length; i++) {
            this.displayMarker(data[i], this.map, bounds)
          }

          this.map.setBounds(bounds)
          if (this.map == ''){
            alert('해당 은행이 없습니다.')
          }
        }
      })
      } else {
        alert('은행을 선택해주세요.')
      }
      
    },
    displayMarker(place, map, bounds) {
      const marker = new kakao.maps.Marker({
        map: map,
        position: new kakao.maps.LatLng(place.y, place.x)
      })

      const infowindow = new kakao.maps.InfoWindow({ zIndex: 1 })
      kakao.maps.event.addListener(marker, 'mouseover', () => {
        infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>')
        infowindow.open(map, marker);
      })
      kakao.maps.event.addListener(marker, 'mouseout', () => {
        infowindow.close();
      })
      kakao.maps.event.addListener(marker, "click", () => {
        // console.log(place);
        // console.log(place.place_url);

        if (confirm(`'${place.place_name}' 홈페이지로 이동하시겠습니까?`)) {
          window.open(place.place_url, "_blank");
        }
      });
      
      bounds.extend(new kakao.maps.LatLng(place.y, place.x))
      this.markers.push(marker);
    },
    // 마지막 단계에 추가한 부분
    clearMarkers() {
      // 기존에 표시된 마커들을 제거
      for (let i = 0; i < this.markers.length; i++) {
        this.markers[i].setMap(null);
      }
      this.markers = [];
    },
  },

}
</script>

<style scoped>
.map-page {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

#map-comp {
  width: 400px;
  height: 400px;
  margin-top: 20px;
  margin-bottom: 10px;
  margin: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  
}
.map-box {
  display: flex;
}
.kakao-filter{
  display: flex;
  flex-direction: row;
  align-items: center; /* 가운데 정렬을 위해 추가 */
  margin-top: 10px;
}
.kakao-select {
  padding: 6px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f7f7f7;
  width: 100%;
  flex-direction: row;
}
button {
  padding: 6px 12px;
  border: none;
  border-radius: 4px;
  background-color: #383838;
  color: #fff;
  cursor: pointer;
  margin-left: 10px; /* 버튼 간격을 위해 추가 */
  flex-direction: row;
}
</style>
