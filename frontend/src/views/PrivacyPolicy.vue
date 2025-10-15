<template>
  <div class="min-h-screen bg-gray-50 py-12">
    <div class="container mx-auto px-4 max-w-4xl">
      <div class="bg-white rounded-lg shadow-lg p-8 md:p-12">
        <h1 class="text-4xl font-bold text-gray-900 mb-8">Política de Privacidad</h1>
        
        <div class="prose prose-lg max-w-none">
          <p class="text-sm text-gray-600 mb-8">Última actualización: {{ currentDate }}</p>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">1. Responsable del tratamiento</h2>
          <p class="mb-4">
            En cumplimiento del Reglamento (UE) 2016/679 del Parlamento Europeo y del Consejo, de 27 de abril de 2016, relativo a la protección de las personas físicas en lo que respecta al tratamiento de datos personales (RGPD) y la Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales (LOPDGDD), le informamos:
          </p>
          <ul class="list-disc pl-6 mb-4">
            <li><strong>Responsable:</strong> Sergio Verdugo Rubio</li>
            <li><strong>NIF:</strong> 77199933L</li>
            <li><strong>Dirección:</strong> Alameda Principal 24, 1</li>
            <li><strong>Email:</strong> <a href="mailto:degubernamental@gmail.com" class="text-primary-600 hover:underline">degubernamental@gmail.com</a></li>
          </ul>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">2. Finalidad del tratamiento</h2>
          <p class="mb-4">
            Los datos personales que nos proporcione serán tratados con las siguientes finalidades:
          </p>
          <ul class="list-disc pl-6 mb-4">
            <li>Gestionar y responder a las consultas que nos envíe a través del formulario de contacto</li>
            <li>Enviar información relacionada con nuestros servicios si ha dado su consentimiento</li>
            <li>Cumplir con las obligaciones legales aplicables</li>
            <li>Mejorar la experiencia del usuario en nuestro sitio web mediante el uso de cookies</li>
          </ul>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">3. Base legal del tratamiento</h2>
          <p class="mb-4">
            El tratamiento de sus datos se basa en:
          </p>
          <ul class="list-disc pl-6 mb-4">
            <li>Su consentimiento expreso (Art. 6.1.a RGPD)</li>
            <li>La ejecución de un contrato o precontrato (Art. 6.1.b RGPD)</li>
            <li>El cumplimiento de obligaciones legales (Art. 6.1.c RGPD)</li>
            <li>Interés legítimo del responsable (Art. 6.1.f RGPD)</li>
          </ul>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">4. Conservación de datos</h2>
          <p class="mb-4">
            Los datos personales se conservarán durante el tiempo necesario para cumplir con la finalidad para la que se recabaron y para determinar las posibles responsabilidades que se pudieran derivar de dicha finalidad y del tratamiento de los datos. Será de aplicación lo dispuesto en la normativa de archivos y documentación.
          </p>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">5. Destinatarios de datos</h2>
          <p class="mb-4">
            No se cederán datos a terceros, salvo obligación legal. Los datos pueden ser tratados por proveedores de servicios que actúan como encargados del tratamiento, quienes estarán obligados a mantener el mismo nivel de protección que nosotros.
          </p>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">6. Derechos del interesado</h2>
          <p class="mb-4">
            Puede ejercer los siguientes derechos en cualquier momento:
          </p>
          <ul class="list-disc pl-6 mb-4">
            <li><strong>Derecho de acceso:</strong> Conocer qué datos personales estamos tratando</li>
            <li><strong>Derecho de rectificación:</strong> Solicitar la corrección de datos inexactos</li>
            <li><strong>Derecho de supresión:</strong> Solicitar la eliminación de sus datos</li>
            <li><strong>Derecho de limitación:</strong> Solicitar la limitación del tratamiento</li>
            <li><strong>Derecho de portabilidad:</strong> Recibir sus datos en formato estructurado</li>
            <li><strong>Derecho de oposición:</strong> Oponerse al tratamiento de sus datos</li>
            <li><strong>Derecho a no ser objeto de decisiones automatizadas</strong></li>
          </ul>
          <p class="mb-4">
            Para ejercer estos derechos, puede enviar un correo electrónico a <a href="mailto:degubernamental@gmail.com" class="text-primary-600 hover:underline">degubernamental@gmail.com</a> adjuntando copia de su DNI o documento identificativo equivalente.
          </p>
          <p class="mb-4">
            Asimismo, le informamos de su derecho a presentar una reclamación ante la Agencia Española de Protección de Datos (<a href="https://www.aepd.es" target="_blank" class="text-primary-600 hover:underline">www.aepd.es</a>) si considera que el tratamiento no se ajusta a la normativa vigente.
          </p>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">7. Seguridad de los datos</h2>
          <p class="mb-4">
            Hemos adoptado medidas técnicas y organizativas apropiadas para garantizar un nivel de seguridad adecuado al riesgo, incluyendo, entre otras, la pseudonimización y el cifrado de datos personales, la capacidad de garantizar la confidencialidad, integridad, disponibilidad y resiliencia permanentes de los sistemas y servicios de tratamiento.
          </p>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">8. Cookies</h2>
          <p class="mb-4">
            Este sitio web utiliza cookies propias y de terceros para mejorar la experiencia de navegación y ofrecer contenidos de interés. Para más información sobre las cookies que utilizamos, consulte nuestra 
            <router-link to="/politica-cookies" class="text-primary-600 hover:underline font-semibold">Política de Cookies</router-link>.
          </p>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">9. Actualización de la política</h2>
          <p class="mb-4">
            Nos reservamos el derecho de modificar la presente política para adaptarla a novedades legislativas o jurisprudenciales. En tales casos, se anunciará en esta página los cambios introducidos con razonable antelación a su puesta en práctica.
          </p>

          <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">10. Contacto</h2>
          <p class="mb-4">
            Si tiene alguna duda sobre esta Política de Privacidad, puede contactarnos en:
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
  name: 'PrivacyPolicy',
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

