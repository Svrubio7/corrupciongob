<template>
  <div class="min-h-screen bg-gray-50 py-12">
    <div class="container mx-auto px-4 max-w-4xl">
      <div class="bg-white rounded-lg shadow-lg p-8 md:p-12">
        <h1 class="text-4xl font-bold text-gray-900 mb-8">Aviso Legal</h1>
        
        <div class="prose prose-lg max-w-none">
          <p class="text-sm text-gray-600 mb-8">Última actualización: {{ currentDate }}</p>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">1. Datos identificativos</h2>
          <p class="mb-4">
            En cumplimiento con el deber de información recogido en artículo 10 de la Ley 34/2002, de 11 de julio, de Servicios de la Sociedad de la Información y del Comercio Electrónico, a continuación se reflejan los siguientes datos:
          </p>
          <ul class="list-disc pl-6 mb-4">
            <li><strong>Titular:</strong> Sergio Verdugo Rubio</li>
            <li><strong>NIF:</strong> 77199933L</li>
            <li><strong>Domicilio:</strong> Alameda Principal 24, 1</li>
            <li><strong>Email de contacto:</strong> <a href="mailto:degubernamental@gmail.com" class="text-primary-600 hover:underline">degubernamental@gmail.com</a></li>
            <li><strong>Sitio Web:</strong> degu.es</li>
          </ul>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">2. Objeto</h2>
          <p class="mb-4">
            El presente sitio web tiene como objetivo proporcionar información y análisis sobre la gestión del dinero público en España, casos de corrupción, auditoría gubernamental y transparencia en las instituciones públicas. Todo el contenido publicado tiene carácter informativo y de opinión.
          </p>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">3. Condiciones de uso</h2>
          <p class="mb-4">
            El acceso y uso de este sitio web implica la aceptación de las presentes condiciones de uso. El usuario se compromete a:
          </p>
          <ul class="list-disc pl-6 mb-4">
            <li>Hacer un uso adecuado y lícito del sitio web</li>
            <li>No utilizar el sitio web con fines ilícitos o lesivos de derechos de terceros</li>
            <li>No introducir virus, programas maliciosos o cualquier otro código que pueda dañar el sistema</li>
            <li>No realizar actividades publicitarias o de explotación comercial sin autorización</li>
            <li>Respetar los derechos de propiedad intelectual e industrial</li>
          </ul>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">4. Propiedad intelectual e industrial</h2>
          <p class="mb-4">
            Todos los contenidos de este sitio web, incluyendo textos, fotografías, gráficos, imágenes, iconos, tecnología, software, diseño gráfico y códigos fuente, son propiedad intelectual de Sergio Verdugo Rubio o de terceros que han autorizado su uso, y están protegidos por las leyes españolas e internacionales de propiedad intelectual e industrial.
          </p>
          <p class="mb-4">
            Queda prohibida la reproducción, distribución, comunicación pública, transformación o cualquier otra actividad que se pueda realizar con los contenidos del sitio web sin autorización expresa del titular.
          </p>
          <p class="mb-4">
            Los usuarios pueden compartir los artículos y contenidos del sitio web con fines informativos, siempre que se cite la fuente y se enlace al artículo original.
          </p>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">5. Responsabilidad de los contenidos</h2>
          <p class="mb-4">
            Los contenidos publicados en este sitio web tienen carácter informativo y de opinión. Si bien nos esforzamos por garantizar la exactitud y actualidad de la información, no podemos garantizar la ausencia de errores ni la actualización permanente de la información publicada.
          </p>
          <p class="mb-4">
            Las opiniones expresadas en los artículos son responsabilidad de sus autores y no necesariamente reflejan la opinión del titular del sitio web.
          </p>
          <p class="mb-4">
            El titular del sitio web se reserva el derecho a modificar, suspender, cancelar o restringir el contenido del sitio web, sin necesidad de previo aviso.
          </p>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">6. Enlaces externos</h2>
          <p class="mb-4">
            Este sitio web puede contener enlaces a sitios web de terceros. El titular del sitio web no se hace responsable del contenido, exactitud o fiabilidad de dichos sitios web, ni de las opiniones expresadas en ellos.
          </p>
          <p class="mb-4">
            Los enlaces se proporcionan únicamente con fines informativos y no implican aprobación o respaldo del contenido enlazado.
          </p>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">7. Protección de datos personales</h2>
          <p class="mb-4">
            El tratamiento de los datos personales de los usuarios se realiza conforme a lo establecido en el Reglamento (UE) 2016/679 (RGPD) y la Ley Orgánica 3/2018 (LOPDGDD). Para más información, consulte nuestra 
            <router-link to="/politica-privacidad" class="text-primary-600 hover:underline font-semibold">Política de Privacidad</router-link>.
          </p>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">8. Cookies</h2>
          <p class="mb-4">
            Este sitio web utiliza cookies para mejorar la experiencia del usuario. Para más información sobre las cookies que utilizamos y cómo gestionarlas, consulte nuestra 
            <router-link to="/politica-cookies" class="text-primary-600 hover:underline font-semibold">Política de Cookies</router-link>.
          </p>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">9. Legislación aplicable y jurisdicción</h2>
          <p class="mb-4">
            Las presentes condiciones se rigen por la legislación española. Para la resolución de cualquier controversia derivada del acceso o uso de este sitio web, las partes se someten expresamente a los Juzgados y Tribunales de España, con renuncia a cualquier otro fuero que pudiera corresponderles.
          </p>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">10. Modificaciones</h2>
          <p class="mb-4">
            El titular del sitio web se reserva el derecho a modificar el presente Aviso Legal en cualquier momento. Se recomienda a los usuarios revisar periódicamente estas condiciones.
          </p>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">11. Contacto</h2>
          <p class="mb-4">
            Para cualquier consulta o sugerencia relacionada con este Aviso Legal o con el sitio web, puede contactarnos en:
          </p>
          <p class="mb-4">
            Email: <a href="mailto:degubernamental@gmail.com" class="text-primary-600 hover:underline">degubernamental@gmail.com</a>
          </p>
        </div>

        <div class="mt-12 pt-8 border-t border-gray-200">
          <router-link to="/" class="inline-block bg-primary-600 hover:bg-primary-700 text-white font-semibold px-6 py-3 rounded-lg transition">
            Volver al inicio
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LegalNotice',
  computed: {
    currentDate() {
      return new Date().toLocaleDateString('es-ES', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })
    }
  }
}
</script>

