/**
 * Utility for managing social media meta tags dynamically
 */

export function updateMetaTags(options = {}) {
  const {
    title = 'Auditando Impuestos',
    description = 'Transparencia en el uso del dinero público en España. Descubre como todos los partidos gastan nuestro dinero.',
    image = '/static/auditandoimpuestologo.png',
    url = window.location.href,
    type = 'website'
  } = options

  // Update document title
  document.title = title

  // Update or create meta tags
  updateMetaTag('meta[name="description"]', 'name', 'description', description)
  updateMetaTag('meta[property="og:title"]', 'property', 'og:title', title)
  updateMetaTag('meta[property="og:description"]', 'property', 'og:description', description)
  updateMetaTag('meta[property="og:image"]', 'property', 'og:image', image)
  updateMetaTag('meta[property="og:url"]', 'property', 'og:url', url)
  updateMetaTag('meta[property="og:type"]', 'property', 'og:type', type)
  updateMetaTag('meta[name="twitter:title"]', 'name', 'twitter:title', title)
  updateMetaTag('meta[name="twitter:description"]', 'name', 'twitter:description', description)
  updateMetaTag('meta[name="twitter:image"]', 'name', 'twitter:image', image)
  updateMetaTag('meta[name="twitter:url"]', 'name', 'twitter:url', url)
}

function updateMetaTag(selector, attribute, value, content) {
  let metaTag = document.querySelector(selector)
  
  if (!metaTag) {
    metaTag = document.createElement('meta')
    metaTag.setAttribute(attribute, value)
    document.head.appendChild(metaTag)
  }
  
  metaTag.setAttribute('content', content)
}

export function updateCaseMetaTags(caseData) {
  if (!caseData) return

  const title = `${caseData.title} - Auditando Impuestos`
  const description = caseData.short_description || 'Documentando todo gasto público cuestionable en España.'
  const image = caseData.main_image || '/static/auditandoimpuestologo.png'
  const url = `${window.location.origin}/app/case/${caseData.slug || caseData.id}`

  updateMetaTags({
    title,
    description,
    image,
    url,
    type: 'article'
  })
}

export function resetMetaTags() {
  updateMetaTags()
}
