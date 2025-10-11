// Simplified world map data with SVG paths for major countries
// In a real implementation, you would use a complete TopoJSON/GeoJSON file
// These are approximate paths for demonstration purposes

export const worldMapPaths = {
  // Europe
  'ESP': 'M 200,220 L 195,215 L 190,218 L 185,220 L 180,225 L 185,230 L 190,232 L 195,230 L 200,228 Z', // Spain
  'FRA': 'M 210,200 L 205,195 L 200,200 L 195,205 L 200,210 L 205,212 L 215,210 L 218,205 L 215,200 Z', // France
  'DEU': 'M 230,195 L 225,190 L 220,195 L 225,200 L 230,202 L 235,200 L 238,195 L 235,190 Z', // Germany
  'ITA': 'M 240,215 L 235,210 L 230,215 L 228,220 L 230,230 L 235,235 L 240,232 L 242,225 L 240,220 Z', // Italy
  'GBR': 'M 195,185 L 190,180 L 185,185 L 190,190 L 195,192 L 200,190 L 202,185 L 200,180 Z', // UK
  'PRT': 'M 180,215 L 175,210 L 170,215 L 172,220 L 175,225 L 180,222 L 182,218 Z', // Portugal
  'NLD': 'M 220,180 L 215,175 L 210,180 L 215,185 L 220,187 L 225,185 L 227,180 Z', // Netherlands
  'BEL': 'M 215,190 L 210,185 L 205,190 L 210,195 L 215,197 L 220,195 L 222,190 Z', // Belgium
  'CHE': 'M 225,205 L 220,200 L 215,205 L 220,210 L 225,212 L 230,210 L 232,205 Z', // Switzerland
  'POL': 'M 250,185 L 245,180 L 240,185 L 245,190 L 250,192 L 255,190 L 258,185 Z', // Poland
  'SWE': 'M 245,150 L 240,145 L 235,150 L 240,160 L 245,165 L 250,160 L 252,150 Z', // Sweden
  'NOR': 'M 235,130 L 230,120 L 225,130 L 230,145 L 235,150 L 240,145 L 242,135 Z', // Norway
  'GRC': 'M 260,235 L 255,230 L 250,235 L 252,240 L 255,245 L 260,242 L 265,237 Z', // Greece
  'RUS': 'M 300,160 L 290,150 L 280,160 L 290,170 L 310,175 L 350,165 L 400,155 L 380,145 L 320,150 Z', // Russia
  
  // Americas
  'USA': 'M 120,190 L 100,185 L 80,195 L 75,210 L 85,225 L 110,230 L 135,220 L 140,210 L 135,195 Z', // USA
  'CAN': 'M 110,140 L 90,130 L 70,140 L 60,160 L 70,175 L 100,180 L 130,170 L 140,155 L 130,145 Z', // Canada
  'MEX': 'M 100,240 L 90,235 L 80,240 L 75,250 L 80,260 L 95,265 L 110,260 L 115,250 L 110,245 Z', // Mexico
  'BRA': 'M 180,320 L 170,310 L 160,320 L 165,340 L 180,360 L 200,365 L 210,350 L 205,330 Z', // Brazil
  'ARG': 'M 165,380 L 160,370 L 155,380 L 160,400 L 170,420 L 180,425 L 185,410 L 180,390 Z', // Argentina
  'CHL': 'M 145,380 L 140,370 L 135,385 L 140,410 L 145,430 L 150,425 L 152,400 L 148,385 Z', // Chile
  'COL': 'M 145,285 L 140,280 L 135,285 L 140,295 L 145,300 L 155,298 L 158,290 L 155,285 Z', // Colombia
  'PER': 'M 145,310 L 140,305 L 135,310 L 140,325 L 145,335 L 155,333 L 158,320 L 155,310 Z', // Peru
  'VEN': 'M 155,280 L 150,275 L 145,280 L 150,290 L 155,295 L 165,293 L 168,285 L 165,280 Z', // Venezuela
  'CUB': 'M 130,255 L 125,250 L 120,255 L 125,260 L 135,262 L 140,258 L 138,255 Z', // Cuba
  
  // Asia
  'CHN': 'M 650,210 L 640,200 L 630,210 L 640,230 L 660,240 L 680,235 L 690,220 L 680,210 Z', // China
  'JPN': 'M 720,215 L 715,210 L 710,215 L 715,230 L 720,240 L 730,238 L 735,225 L 730,215 Z', // Japan
  'IND': 'M 570,265 L 560,255 L 550,265 L 555,285 L 570,295 L 585,290 L 590,275 L 585,265 Z', // India
  'KOR': 'M 700,215 L 695,210 L 690,215 L 695,225 L 700,230 L 708,228 L 710,220 L 708,215 Z', // South Korea
  'IDN': 'M 620,320 L 610,315 L 600,325 L 610,340 L 630,345 L 650,340 L 660,330 L 650,320 Z', // Indonesia
  'THA': 'M 600,280 L 595,275 L 590,280 L 595,295 L 600,305 L 610,303 L 613,290 L 610,280 Z', // Thailand
  'TUR': 'M 280,215 L 275,210 L 270,215 L 275,225 L 285,230 L 295,228 L 300,220 L 295,215 Z', // Turkey
  'SAU': 'M 340,270 L 330,265 L 320,270 L 325,285 L 340,295 L 355,290 L 360,280 L 355,270 Z', // Saudi Arabia
  'IRN': 'M 350,245 L 340,240 L 330,245 L 335,260 L 350,270 L 365,265 L 370,255 L 365,245 Z', // Iran
  
  // Africa
  'ZAF': 'M 270,380 L 260,375 L 250,380 L 255,395 L 270,405 L 285,400 L 290,390 L 285,380 Z', // South Africa
  'EGY': 'M 270,255 L 265,250 L 260,255 L 265,270 L 270,280 L 280,278 L 285,268 L 280,255 Z', // Egypt
  'NGA': 'M 220,290 L 215,285 L 210,290 L 215,305 L 220,315 L 230,313 L 235,303 L 230,290 Z', // Nigeria
  'MAR': 'M 195,250 L 190,245 L 185,250 L 190,260 L 195,265 L 205,263 L 208,255 L 205,250 Z', // Morocco
  'DZA': 'M 210,250 L 205,245 L 200,250 L 205,265 L 215,275 L 230,273 L 235,260 L 230,250 Z', // Algeria
  'KEN': 'M 285,305 L 280,300 L 275,305 L 280,320 L 285,330 L 295,328 L 300,318 L 295,305 Z', // Kenya
  
  // Oceania
  'AUS': 'M 720,360 L 700,350 L 680,360 L 690,385 L 720,400 L 750,395 L 770,380 L 760,365 Z', // Australia
  'NZL': 'M 800,405 L 795,400 L 790,405 L 795,420 L 800,430 L 810,428 L 815,418 L 810,405 Z', // New Zealand
}

// Helper function to get country name from code
export function getCountryName(code) {
  const countryNames = {
    'ESP': 'España',
    'FRA': 'Francia',
    'DEU': 'Alemania',
    'ITA': 'Italia',
    'GBR': 'Reino Unido',
    'PRT': 'Portugal',
    'NLD': 'Países Bajos',
    'BEL': 'Bélgica',
    'CHE': 'Suiza',
    'POL': 'Polonia',
    'SWE': 'Suecia',
    'NOR': 'Noruega',
    'GRC': 'Grecia',
    'RUS': 'Rusia',
    'USA': 'Estados Unidos',
    'CAN': 'Canadá',
    'MEX': 'México',
    'BRA': 'Brasil',
    'ARG': 'Argentina',
    'CHL': 'Chile',
    'COL': 'Colombia',
    'PER': 'Perú',
    'VEN': 'Venezuela',
    'CUB': 'Cuba',
    'CHN': 'China',
    'JPN': 'Japón',
    'IND': 'India',
    'KOR': 'Corea del Sur',
    'IDN': 'Indonesia',
    'THA': 'Tailandia',
    'TUR': 'Turquía',
    'SAU': 'Arabia Saudita',
    'IRN': 'Irán',
    'ZAF': 'Sudáfrica',
    'EGY': 'Egipto',
    'NGA': 'Nigeria',
    'MAR': 'Marruecos',
    'DZA': 'Argelia',
    'KEN': 'Kenia',
    'AUS': 'Australia',
    'NZL': 'Nueva Zelanda'
  }
  
  return countryNames[code] || code
}

