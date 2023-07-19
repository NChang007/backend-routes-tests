const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			token: null,
			backurl: 'https://nchang007-automatic-enigma-q5gpvj6699rc9pr7-3001.preview.app.github.dev',
			discussions: [],
		},
		actions: {
			login: async (email, password) => {
				const store = getStore();
				try {
				  const response = await fetch(store.apiUrl + "/api/login", {
					method: "POST",
					body: JSON.stringify({
					  email: email,
					  password: password
					}),
					headers: {
					  "Content-Type": "application/json"
					}
				  });
		
				  const data = await response.json();
				  if (response.ok) {
					setStore({
					  token: data.token
					});
					localStorage.setItem("token", JSON.stringify(body.token));
					localStorage.setItem("user", JSON.stringify(body.user));
					return body;
				  } else {
					console.log("Log in unsuccessful");
				  }
				} catch (error) {
				  console.log(error);
				}
			},

			syncSessionToStore: () => {
				let ssToken = sessionStorage.getItem('token')

				setStore({ token:ssToken })
			},

			getAllDiscussions: () => {
				let backurl = getStore().backurl
				fetch(backurl + "/api/discussions")
				.then((res) => res.json())
				.then((data) => {
					setStore({ discussions: data });
				})
				.catch((error) => {
					console.error("GET ALL DISCUSSIONS flux",error);
				});
			},
			

			// this is the end of actions
		}
	};
};

export default getState;
