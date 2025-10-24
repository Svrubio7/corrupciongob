<template>
  <div class="bg-white rounded-xl shadow hover:shadow-lg transition overflow-hidden flex flex-col h-full">
    <router-link :to="`/app/case/${caseData.slug || caseData.id}`" class="block">
      <img
        v-if="caseData.main_image"
        :src="caseData.main_image"
        :alt="caseData.title"
        class="w-full h-48 object-cover"
      />
      <div v-else class="w-full h-48 bg-gray-200 flex items-center justify-center text-gray-400">
        Sin imagen
      </div>
      <div class="p-4 flex-1 flex flex-col">
        <h3 class="text-lg font-bold text-gray-900 mb-2">{{ caseData.title }}</h3>
        <p class="text-gray-600 text-sm mb-4 line-clamp-3">{{ caseData.short_description }}</p>
        <div class="mt-auto">
          <div class="flex items-center justify-between mb-2">
            <span v-if="caseData.amount" class="text-primary-600 font-semibold">€{{ formatAmount(caseData.amount) }}</span>
            <span v-else-if="caseData.publication_type === 'case'" class="text-gray-500 font-semibold">Sin importe</span>
          </div>
          <div class="flex justify-end">
            <span v-if="caseData.date" class="text-xs text-gray-500">{{ formatDate(caseData.date) }}</span>
          </div>
        </div>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'CaseCard',
  props: {
    caseData: { type: Object, required: true },
    large: { type: Boolean, default: false }
  },
  methods: {
    formatAmount(amount) {
      return new Intl.NumberFormat('es-ES').format(amount)
    },
    formatDate(dateString) {
      return new Date(dateString).toLocaleDateString('es-ES', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })
    }
  }
}
</script>

<style scoped>
/* Optional: make the card larger if 'large' prop is true */
:host([large]) .h-48 {
  height: 18rem;
}
</style>