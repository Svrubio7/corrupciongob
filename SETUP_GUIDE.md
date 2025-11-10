# Quick Setup Guide

## 🚀 Getting Started

Follow these steps to test the new features locally:

### 1. Backend Setup

```bash
# Navigate to project root
cd "c:\Users\svrub\Documents\Mis cosillas\ProyectosPersonales\corrupciongob"

# Activate virtual environment
.\venv\Scripts\activate

# Run migrations to add yearly amount fields
python manage.py migrate

# Create development data (3 casos + 3 articles)
python manage.py create_dev_data

# Start Django development server
python manage.py runserver
```

### 2. Frontend Setup

Open a new terminal:

```bash
# Navigate to frontend directory
cd "c:\Users\svrub\Documents\Mis cosillas\ProyectosPersonales\corrupciongob\frontend"

# Install dependencies (includes Chart.js)
npm install

# Start Vite development server
npm run dev
```

### 3. Access the Application

- **Frontend:** http://localhost:5173
- **Backend API:** http://localhost:8000

## 📋 What to Test

### Landing Page (http://localhost:5173)
- ✅ Dual carousels for Casos and Publicaciones
- ✅ Auto-rotation every 3 seconds
- ✅ Manual navigation with arrows
- ✅ Dot indicators
- ✅ Click to view details
- ✅ Desktop: side by side | Mobile: stacked

### Analytics Page (http://localhost:5173/analytics)
- ✅ Overview cards (Total Cases, Total Amount)
- ✅ Money per Year chart (2018-2025)
- ✅ Money by Political Party (donut chart)
- ✅ Money by Institution Type (pie chart)
- ✅ Money by Country (horizontal bar)
- ✅ Money by Corruption Type (horizontal bar)
- ✅ Money by Region (horizontal bar)
- ✅ Top 10 Cases by Amount (donut chart)
- ✅ Detailed data tables with percentages

### Admin Panel (http://localhost:8000/admin)
- ✅ Login with your admin credentials
- ✅ Edit a case/publication
- ✅ See "Importes por Año (2018-2025)" section (collapsed by default)
- ✅ Add amounts for specific years
- ✅ Save and verify changes appear in analytics

## 🔧 Troubleshooting

### Issue: Frontend shows "No hay casos/publicaciones disponibles"
**Solution:** Make sure you ran `python manage.py create_dev_data`

### Issue: Charts don't render
**Solution:** 
1. Check console for errors
2. Make sure `npm install` was run
3. Verify Chart.js is installed: `npm list chart.js`

### Issue: Analytics page shows 0 for everything
**Solution:** 
1. Check that backend is running on port 8000
2. Verify API endpoint works: http://localhost:8000/api/cases/analytics/
3. Check browser console for CORS or network errors

### Issue: Carousel doesn't auto-play
**Solution:** This is expected behavior if there's only 1 item. Add more cases/publications via admin.

## 📊 Sample Data Structure

The dev data includes:

**3 Casos:**
1. Malversación de Fondos Municipales - €2.5M (2020-2023)
2. Contratos Fraudulentos - €5M (2019-2022)
3. Despilfarro en Gastos de Representación - €1.2M (2021-2024)

**3 Articles:**
1. Análisis del Gasto Público en 2023
2. La Importancia de la Transparencia Gubernamental (Opinion)
3. Informe sobre Contratación Pública 2023 (Report)

## 🎨 Features Highlights

### Yearly Amount Breakdown
- Each case can have specific amounts for years 2018-2025
- Allows granular analysis of spending over time
- Analytics page uses this data for yearly charts

### Interactive Carousels
- 3-second auto-rotation with smooth fade
- Pause on hover/interaction
- Restart after manual navigation
- Consistent aspect ratio across devices

### Beautiful Charts
- 8 different visualization types
- Interactive tooltips with currency formatting
- Color-coded by categories
- Responsive and mobile-friendly

## 🔐 Environment Variables

Make sure these are set in your `.env` file:

```bash
# Backend
DJANGO_DEBUG=True
VITE_API_BASE_URL=http://localhost:8000/api/

# Frontend (.env in frontend/)
VITE_API_BASE_URL=http://localhost:8000/api/
```

## 📱 Mobile Testing

To test on mobile devices on your local network:

1. Find your local IP: `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
2. Update `VITE_API_BASE_URL` to use your local IP
3. Run frontend with: `npm run dev -- --host`
4. Access from mobile: `http://YOUR_IP:5173`

## ✨ Production Deployment

When ready to deploy:

1. Run migrations on production:
   ```bash
   python manage.py migrate
   ```

2. Build frontend:
   ```bash
   cd frontend
   npm run build
   ```

3. Collect static files:
   ```bash
   python manage.py collectstatic --noinput
   ```

4. **DO NOT** run `create_dev_data` in production (it's blocked by DEBUG check)

## 🆘 Need Help?

If you encounter any issues:
1. Check the browser console for errors
2. Check Django terminal for backend errors
3. Verify all migrations are applied
4. Ensure dev data was created successfully
5. Try clearing browser cache
6. Restart both frontend and backend servers

---

## ✅ All Done!

Your application now has:
- ✅ Beautiful dual carousels on landing page
- ✅ Comprehensive analytics dashboard with 8+ charts
- ✅ Yearly amount tracking (2018-2025)
- ✅ Sample dev data for testing
- ✅ Responsive design on all devices

Enjoy exploring the new features! 🎉

