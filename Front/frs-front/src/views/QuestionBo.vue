<template>
  <div id="question-page" class="container">
    <div class="menu-links">
      <router-link to="/article" class="menu-link">자유게시판</router-link> <div class="menu-link">|</div>
      <router-link to="/question" class="menu-link">자주 묻는 질문</router-link> <div class="menu-link">|</div>
      <router-link to="/onetoone" class="menu-link">1:1 문의</router-link> 
    </div><hr>
      <b-row>
        <b-col class="d-flex align-items-center mt-3">
          <h2 class="section-title">자주 묻는 질문</h2>
          <!-- <b-button style="font-family: 'ONE-Mobile-Title';" class="create-button ms-auto" href="/onetoonecreate">문의하기</b-button> -->
        </b-col>
      </b-row>
      <br><hr>
    <div class="faq-section">
      <div class="faq-list">
        <b-card no-body class="mb-3" v-for="(item, index) in faqList" :key="index">
          <b-card-header header-tag="header" class="p-1" style="cursor: pointer;" role="tab" v-b-toggle="'collapse-' + (index + 1)">
            <div block variant="light" class="text-left">
              <div class="text-left header-body" role="tab">{{ item.question }}</div>
            </div>
          </b-card-header>
          <b-collapse :id="'collapse-' + (index + 1)" accordion="question-accordion" role="tabpanel">
            <b-card-body class="questioncard-body">
              {{ item.answer }}
            </b-card-body>
          </b-collapse>
        </b-card>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'QuestionBoard',
  data() {
    return {
      faqList: [
        {
          question: '1. 예금과 적금의 기본 개념과 차이점은 무엇인가요?',
          answer: '예금은 은행에 돈을 맡겨 예금액에 대해 이자를 받는 것을 의미합니다. 적금은 특정 기간 동안 정해진 금액을 일정한 주기로 저축하고, 이자를 받는 저축상품입니다. 예금은 언제든지 인출할 수 있지만, 적금은 일정한 기간 동안 해지하지 않고 유지해야 합니다.',
        },
        {
          question: '2. 예금 상품의 종류는 어떤 것들이 있나요?',
          answer: '예금 상품에는 일반 예금, 정기 예금, 적금, 체크카드 예금 등이 있습니다. 일반 예금은 일반적인 예금 상품으로 이자를 받을 수 있으며, 인출이 자유로운 상품입니다. 정기 예금은 예금 기간과 이자율이 미리 정해진 상품입니다. 적금은 정해진 기간 동안 일정한 금액을 저축하고, 이자를 받는 상품입니다. 체크카드 예금은 예금과 동시에 체크카드를 발급받아 현금 인출이 가능한 상품입니다.',
        },
        {
          question: '3. 적금 상품의 장단점은 무엇인가요?',
          answer: '적금의 장점으로는 꾸준한 저축을 통해 목표 금액을 모을 수 있다는 점과 저리율에 따라 이자를 받을 수 있다는 점이 있습니다. 단점으로는 일정 기간 동안 금액을 출금할 수 없거나 중도 해지 시 일부 이자 손실이 발생할 수 있다는 점입니다.',
        },
        {
          question: '4. 예금이나 적금을 선택할 때 고려해야 할 요소는 무엇인가요?',
          answer: '예금이나 적금을 선택할 때 고려해야 할 요소로는 목표 금액과 기간, 이자율, 예금 상품의 특징, 예금의 유연성 등이 있습니다. 목표 금액과 기간에 맞게 저축할 수 있는 상품을 선택하고, 이자율과 상품의 특징을 비교하여 최적의 상품을 선택하는 것이 중요합니다.',
        },
        {
          question: '5. 예금이나 적금을 어떻게 개설하나요?',
          answer: '예금이나 적금을 개설하기 위해서는 은행이나 금융기관을 방문하거나 온라인으로 신청을 진행할 수 있습니다. 개설에 필요한 신분증, 주민등록등본, 기타 필요한 서류를 제출하고 개설 신청서를 작성해야 합니다. 온라인 신청의 경우에는 인터넷 뱅킹이나 모바일 앱을 통해 간편하게 개설할 수 있습니다.',
        },
        {
          question: '6. 예금이나 적금의 이자율은 어떻게 결정되나요?',
          answer: '예금이나 적금의 이자율은 시장 금리, 경기 상황, 금융기관의 정책 등에 의해 결정됩니다. 일반적으로 경기가 호조일 때는 이자율이 상승하고, 경기가 침체할 때는 이자율이 하락하는 경향이 있습니다. 각 금융기관은 경쟁력을 갖추기 위해 이자율을 조정하기도 합니다.',
        },
        {
          question: '7. 예금이나 적금에서의 이자 지급 방식은 어떤 것들이 있나요?',
          answer: '예금이나 적금의 이자 지급 방식에는 매월 이자 지급, 분기별 이자 지급, 만기 시 이자 지급 등이 있습니다. 이자 지급 방식은 예금 상품에 따라 다를 수 있으며, 개설 시에 확인해야 합니다.',
        },
        {
          question: '8. 예금이나 적금을 중도 해지하면 어떻게 되나요?',
          answer: '예금이나 적금을 중도 해지할 경우에는 일정한 이자 손실이 발생할 수 있습니다. 예금 상품에 따라 해지 수수료가 있을 수도 있으니, 개설 시에 상세한 해지 조건을 확인하는 것이 좋습니다.',
        },
        {
          question: '9. 예금이나 적금에서 세금이 발생하나요?',
          answer: '예금이나 적금에서 발생하는 세금은 국가 및 지방세에 따라 다를 수 있습니다. 이자 수익에 대해 소득세가 부과될 수 있으며, 세금의 금액과 세금 부과 기준은 국가의 세법에 따라 결정됩니다.',
        },
      ],
    };
  },
};
</script>

<style scoped>
#question-page{
  margin-bottom: 100px;
}
.menu-links {
  display: flex;
  justify-content: center;
}

.menu-link {
  color: #333;
  font-size: 18px;
  text-decoration: none;
  padding: 10px;
  margin-right: 10px;
  transition: color 0.3s;
}

.menu-link:hover {
  border-bottom-color: #555;
}
.menu-link:hover,
.menu-link.active {
  color: #9bb5d1;
}
.menu-link:hover,
.menu-link.active {
  color: #007bff;
}
.section-title {
  font-family: 'TheJamsil5Bold';
  font-size: 30px;
  font-weight: bold;
  margin-bottom: 20px;
}

.faq-list {
  margin-top: 20px;
}

.card-body {
  padding: 10px;
}


.card-body {
  padding: 10px;
  margin: 0 auto; /* 가운데 정렬을 위해 추가 */
}
</style>