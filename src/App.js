import { count_triangles } from 'components/count_triangles'
import { ThemeProvider } from 'styled-components'
import { darkTheme } from 'theme'
import { GlobalStyles } from 'global'
import { binary_gap } from 'components/binary_gap'
import { permutator } from 'components/permutator'
import { max_counters } from 'components/max_counters'
import { find5thBigNum } from 'components/find5thBigNum'
import { tie_ropes } from 'components/tie_ropes'
import { odd_occurrences } from 'components/odd_occurrences'
import { max_product_three } from 'components/max_product_three'

function App() {
  return (
    <ThemeProvider theme={{ ...darkTheme }}>
      <>
        <GlobalStyles />
        <div className='App'>
          <div>
            result
            <ul>
              <li>
                {/* count_triangles([10, 2, 5, 1, 8, 20]) ={'>'}{' '}
                // {count_triangles([10, 2, 5, 1, 8, 20]).toString()} */}
                {/* binary_gap(9) = {binary_gap(9)} */}
                {/* {find5thBigNum([33, 55, 13, 46, 87, 42, 10, 34, 43, 56]).toString()} */}
                {/* {odd_occurrences([9, 3, 9, 1, 3, 9, 7, 9]).toString()} */}
                {/* {max_product_three().toString()} */}
              </li>
            </ul>
          </div>
        </div>
      </>
    </ThemeProvider>
  )
}

export default App
