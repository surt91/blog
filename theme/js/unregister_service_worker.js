if ('serviceWorker' in navigator) {
    navigator.serviceWorker.getRegistrations().then(
        function(registrations) {
            for(let registration of registrations) {
                console.log("unregister", registration)
                registration.unregister();
            }
        });
}