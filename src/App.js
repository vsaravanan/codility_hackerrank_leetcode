import { count_triangles } from 'components/count_triangles'
import { ThemeProvider } from 'styled-components'
import { darkTheme } from 'theme'
import { GlobalStyles } from 'global'
import { binary_gap } from 'components/binary_gap'
import { permutator } from 'components/permutator'

function App() {
  return (
    <ThemeProvider theme={{ ...darkTheme }}>
      <>
        <GlobalStyles />
        <div className='App'>
          <div>
            count triangles
            <ul>
              <li>
                {/* count_triangles([10, 2, 5, 1, 8, 20]) ={'>'}{' '}
                {count_triangles([10, 2, 5, 1, 8, 20]).toString()} */}
                {/* binary_gap(9) = {binary_gap(9)} */}
              </li>
            </ul>
          </div>
        </div>
      </>
    </ThemeProvider>
  )
}

export default App
