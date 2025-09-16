/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        palette: {
          light: '#FEFCFA',     // Very light cream (from Coolors)
          beige: '#EBC2BB',     // Light pink/beige (from Coolors)
          taupe: '#D62F25',     // Red accent (from Coolors)
          black: '#000000',     // Dark gray for text
          primary: '#D62F25',   // Red primary (from Coolors)
          secondary: '#FDCC11', // Yellow/Gold accent (from Coolors)
          accent: '#EBC2BB',    // Light pink/beige accent
          white: '#FFFFFF',     // Pure white (from Coolors)
        },
        // You can keep or remove primary/secondary if you want
      },
      fontFamily: {
        sans: ['Montserrat', 'system-ui', 'sans-serif'],
        'inter': ['Inter', 'system-ui', 'sans-serif'],
        'poppins': ['Poppins', 'system-ui', 'sans-serif'],
        'montserrat': ['Montserrat', 'system-ui', 'sans-serif'],
        'source-sans': ['Source Sans Pro', 'system-ui', 'sans-serif'],
        'lora': ['Lora', 'serif'],
        'crimson': ['Crimson Text', 'serif'],
      },
    },
  },
  plugins: [],
}

