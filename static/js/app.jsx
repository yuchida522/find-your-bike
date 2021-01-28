"use strict";

function App() {
	return (
		<Router>
        <div><NavComponent/></div>
			<Switch>
				<Route exact path='/login'>
					<Login />
				</Route>
<<<<<<< HEAD
				<Route exact path='/profile'>
					<Profile />
				</Route>

                <Route exact path='/navbar'>
					<Login />
				</Route>

=======
>>>>>>> c2a3a28 (move navbar above Switch)
			</Switch>
		</Router>	
	);
}


ReactDOM.render(<App />, document.getElementById('app'))