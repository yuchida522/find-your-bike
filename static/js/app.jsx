"use strict";

function App() {
	return (
		<Router>
			<Switch>
				<Route exact path='/login'>
					<Login />
				</Route>
				<Route exact path='/profile'>
					<Profile />
				</Route>
			</Switch>
		</Router>	
	);
}


ReactDOM.render(<App />, document.getElementById('app'))