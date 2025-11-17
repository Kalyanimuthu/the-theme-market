module.exports = {
  content: [
    "./templates/**/*.{html,js}",
    "./**/templates/**/*.html",
    "./static/**/**/*.{js,html}",
  ],
  theme: {
    extend: {
      colors: {
        purpleDark: "#431A97",
        greenBright: "#76C01D",
        blueDeep: "#0056B3",
      },
      fontFamily: {
      poppins: ['Poppins', 'sans-serif'],
      inter: ['Inter', 'sans-serif'],
    },

  
keyframes: {
  
  zoomPulse: {
    "0%, 100%": { transform: "scale(1)" },
    "50%": { transform: "scale(1.1)" },
  },
  floatUpDown: {
    "0%, 100%": { transform: "translateY(0)" },
    "50%": { transform: "translateY(-12px)" },
  },
  fadeIn: {
    "0%, 100%": { opacity: "0"; transform: "scale(0.95)" },
    "50%": { opacity: "1"; transform: "scale(1)" },
  },
  
  badgePulse: {
    "0%":   { transform: "scale(1)",   opacity: "1"   },
    "50%":  { transform: "scale(1.06)",opacity: "0.5" },
    "100%": { transform: "scale(1)",   opacity: "1"   },
  },
},
animation: {
  zoomPulse: "zoomPulse 2s ease-in-out infinite",
  floatUpDown: "floatUpDown 2s ease-in-out infinite",
  badgePulse: "badgePulse 2s ease-in-out infinite",
 fadeIn: "fadeIn 0.3s ease-out",
},

    },
  },
  plugins: [],
};
