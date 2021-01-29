"use strict";

function App() {
	return (
		<Router>
        <div><NavComponent/></div>
			<Switch>
				<Route exact path='/login'>
					<Login />
				</Route>

                <Route exact path='/about'>
					<About />
                </Route>

                <Route exact path='/profile'>
				    <Profile />
 				</Route>
                <Route exact path='/navbar'>
                    <NavComponent />
                </Route>

			</Switch>
        </Router>
    );
}


ReactDOM.render(<App />, document.getElementById('app'))



