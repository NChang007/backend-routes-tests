const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			backurl: 'https://nchang007-automatic-enigma-q5gpvj6699rc9pr7-3001.preview.app.github.dev',
			discussions: [],
		},
		actions: {
			getAllDiscussions: () => {
				let backurl = getStore().backurl
				fetch(backurl + "/api/discussions")
				.then((res) => res.json())
				.then((data) => {
					console.log(data);
					setStore({ discussions: data });
					console.log(getStore().discussions);
				})
				.catch((error) => {
					console.log(error);
				});
			},
			

			// this is the end of actions
		}
	};
};

export default getState;
